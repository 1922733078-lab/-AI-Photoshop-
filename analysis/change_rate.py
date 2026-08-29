#!/usr/bin/env python3
"""整图变化率C计算脚本（论文表5复现用）。

定义：C = |{(x,y): ||O(x,y)-I(x,y)||_2 > tau}| / (W*H)
其中 O=输出图像, I=基准图像, 二者统一重采样到基准图像尺寸的网格(LANCZOS), tau为变化阈值(0-255标度)。
运行: python3 change_rate.py   (在仓库根目录执行, 需 PIL/numpy)
"""
from PIL import Image
import numpy as np, os, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(REPO, "experiments")
TAUS = (20, 30, 40)

def c(a_path, b_path, tau):
    """a=输出, b=基准; 网格取基准图像尺寸"""
    bi = Image.open(b_path); W, H = bi.size
    A = np.asarray(Image.open(a_path).convert("RGB").resize((W, H), Image.LANCZOS), dtype=np.int32)
    B = np.asarray(bi.convert("RGB").resize((W, H), Image.LANCZOS), dtype=np.int32)
    return round(float((np.sqrt(((A - B) ** 2).sum(axis=2)) > tau).mean()) * 100, 1)

def row(label, base, out):
    return {"任务(基准)": label, **{p: {f"tau{t}": c(out[p], base, t) for t in TAUS} for p in out}}

def main():
    o = lambda *p: os.path.join(EXP, *p)
    orig = {t: o("photoshop_2026", "00_originals", f + ".jpg") for t, f in
            [("删除杂物","删除杂物"),("添加物品","添加物品"),("扩展画面","扩展画面"),("更换背景","替换背景")]}
    outs = {
      "删除杂物": {"PS2026": o("photoshop_2026","01_delete_object","delete_object_ps2026_result.png"),
                "千问": o("qwen_20260512","01_delete_object","删除杂物的生成图.png"),
                "即梦": o("jimeng","01_delete_object","删除物品的生成结果.png"),
                "豆包": o("doubao","01_delete_object","删除杂物的生成结果.png")},
      "添加物品": {"PS2026": o("photoshop_2026","02_add_cup","add_cup_ps2026_round1_result.png"),
                "千问": o("qwen_20260512","02_add_cup","增加物品生成图.png"),
                "即梦": o("jimeng","02_add_cup","增加物品的生成结果图.png"),
                "豆包": o("doubao","02_add_cup","增加物品的生图结果.png")},
      "更换背景": {"PS2026": o("photoshop_2026","04_replace_background","生成的结果图片.png"),
                "千问": o("qwen_20260512","04_replace_background","更换背景的生成图.png"),
                "即梦": o("jimeng","04_replace_background","更换背景生成图片.png"),
                "豆包": o("doubao","04_replace_background","更换背景的生图结果.png")},
    }
    sec = {"PS2026": o("photoshop_2026","05_second_round","add_cup_second_round_final.png"),
           "千问": o("qwen_20260512","05_second_round","二次修改生成图.png"),
           "即梦": o("jimeng","05_second_round","二次修改生成图.png"),
           "豆包": o("doubao","05_second_round","二次编辑生成图片.png")}
    res = []
    res.append(row("删除杂物(对原图)", orig["删除杂物"], outs["删除杂物"]))
    res.append(row("添加物品(对原图)", orig["添加物品"], outs["添加物品"]))
    res.append(row("更换背景(对原图)", orig["更换背景"], outs["更换背景"]))
    res.append(row("二次编辑-二轮对各自一轮结果", outs["添加物品"]["PS2026"],
                   {p: sec[p] for p in sec}))  # 基准按列取各自一轮结果
    # 二次编辑"对各自一轮结果"需逐列基准, 单独计算:
    res[-1] = {"任务(基准)": "二次编辑(二轮对各自一轮结果)",
               **{p: {f"tau{t}": c(sec[p], outs["添加物品"][p], t) for t in TAUS} for p in sec}}
    res.append(row("二次编辑(二轮对原图)", orig["添加物品"], sec))
    print(json.dumps(res, ensure_ascii=False, indent=1))
    with open(os.path.join(REPO, "analysis", "change_rate_results.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
