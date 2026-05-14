# 每一步详细操作指南

本文档面向想要完整复现本仓库实验的人，按实际操作顺序说明如何准备文件、使用 Photoshop 2026 完成创成式填充任务、记录过程截图、导出结果，并与千问、即梦、豆包结果进行对照。

如果只想了解实验设计，可先看 `docs/EXPERIMENT_PROTOCOL.md`。如果要跟着一步一步做，优先使用本文档。

## 1. 准备工作

### 1.1 获取仓库

1. 打开终端。
2. 进入希望保存项目的位置，例如桌面：

```bash
cd ~/Desktop
```

3. 克隆仓库：

```bash
git clone https://github.com/1922733078-lab/-AI-Photoshop-.git AI-Photoshop
cd AI-Photoshop
```

4. 查看目录是否完整：

```bash
ls
```

应能看到：

```text
README.md
docs/
experiments/
scripts/
checksums/
```

### 1.2 还原超大 PSD 文件

GitHub 不允许普通仓库上传超过 100 MB 的单个文件，因此删除杂物任务的 PSD 以分卷形式保存。克隆后执行：

```bash
bash scripts/reconstruct_large_files.sh
```

执行后应生成：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd
```

如需校验文件完整性，执行：

```bash
bash scripts/verify_checksums.sh
```

### 1.3 准备软件和账号

1. 安装并打开 Adobe Photoshop 2026。
2. 登录可使用创成式填充功能的 Adobe 账号。
3. 确认网络可正常连接 Adobe 生成式服务。
4. 在 Photoshop 中确认能看到上下文任务栏中的“创成式填充”。
5. 建议使用原始中文文件名，不要在复现实验前重命名样品图，避免路径记录不一致。

### 1.4 建议的截图命名规则

复现实验时，每一个关键动作都保存截图，命名格式建议为：

```text
01_打开并选择目标.png
02_打开创成式填充.png
03_输入提示词.png
04_点击生成并等待.png
05_生成完成图层.png
```

本仓库现有截图采用英文和中文混合命名，核心原则是保留步骤编号，让读者能按顺序复盘。

## 2. 样品图位置

所有实验样品位于：

```text
experiments/samples/
```

Photoshop 组使用的原图副本位于：

```text
experiments/photoshop_2026/00_originals/
```

每个平台也保存了同一批原图副本，便于确认对照条件一致：

```text
experiments/qwen_20260512/00_originals/
experiments/jimeng/00_originals/
experiments/doubao/00_originals/
```

## 3. Photoshop 2026 总体操作规范

每个 Photoshop 任务都按以下通用流程执行：

1. 打开对应原图。
2. 根据任务目标建立局部选区或主体选区。
3. 点击上下文任务栏中的“创成式填充”。
4. 输入与任务一致的提示词。
5. 点击“生成”。
6. 等待 Photoshop 返回生成结果。
7. 在图层面板中确认生成内容以独立图层形式存在。
8. 检查边缘、光影、透视、纹理连续性和主体是否被误改。
9. 保留过程截图。
10. 导出最终 PNG。
11. 保存 PSD 分层文件。

记录重点不是只保存“最好看的结果”，而是保存从选区、提示词、生成等待、图层结果到二次编辑的完整链路。

## 4. 任务一：删除杂物

### 4.1 任务目标

删除街景图片中的垃圾桶或杂物，并自然补全地面、背景和阴影。

原图路径：

```text
experiments/photoshop_2026/00_originals/删除杂物.jpg
```

现有过程截图目录：

```text
experiments/photoshop_2026/01_delete_object/
```

### 4.2 详细步骤

1. 打开 Photoshop 2026。
2. 选择“文件” -> “打开”。
3. 打开 `experiments/photoshop_2026/00_originals/删除杂物.jpg`。
4. 放大画面，确认需要删除的垃圾桶位置。
5. 选择矩形选框工具。
6. 框选垃圾桶及其周围少量背景区域。
7. 选区不要贴得太紧，建议给目标四周留出一定上下文，让模型能判断地面纹理和光影关系。
8. 保存截图，对应本仓库文件：

```text
experiments/photoshop_2026/01_delete_object/01_open_and_select_garbage.png
```

9. 点击上下文任务栏中的“创成式填充”。
10. 保存创成式填充对话或任务栏截图：

```text
experiments/photoshop_2026/01_delete_object/02_generative_fill_dialog.png
```

11. 在提示词输入框中输入：

```text
删除画面中的垃圾桶，并自然补全背景，保持光影和透视一致
```

12. 保存提示词截图：

```text
experiments/photoshop_2026/01_delete_object/03_prompt_entered_cgevent.png
experiments/photoshop_2026/01_delete_object/03_prompt_entered_manual_check.png
```

13. 点击“生成”。
14. 等待 Photoshop 处理，期间保存等待或处理中截图：

```text
experiments/photoshop_2026/01_delete_object/04_generate_clicked_processing.png
experiments/photoshop_2026/01_delete_object/04_after_generation_wait.png
experiments/photoshop_2026/01_delete_object/05_generate_pressed_return.png
```

15. 生成完成后查看图层面板，确认出现生成图层。
16. 保存生成完成截图：

```text
experiments/photoshop_2026/01_delete_object/06_generation_complete_layers.png
```

17. 关闭或隐藏生成图层，检查原图是否仍可恢复。
18. 保存图层隐藏对照截图：

```text
experiments/photoshop_2026/01_delete_object/07_generated_layer_hidden_original_restored.png
```

19. 检查最终结果是否满足以下条件：
    - 垃圾桶主体消失。
    - 地面纹理连续。
    - 阴影方向不突兀。
    - 没有明显糊块、重复纹理或边缘断裂。
20. 选择“文件” -> “导出” -> “导出为”，保存 PNG。
21. 最终 PNG 应保存为：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_result.png
```

22. 选择“文件” -> “存储为”，保存 PSD 分层文件。
23. PSD 文件路径为：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd
```

24. 如果 PSD 超过 GitHub 单文件限制，按本仓库方式拆分到：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd.parts/
```

## 5. 任务二：添加物品

### 5.1 任务目标

在桌面右侧添加白色陶瓷咖啡杯，并保持透视、接触阴影和整体光影真实。

原图路径：

```text
experiments/photoshop_2026/00_originals/添加物品.jpg
```

过程截图目录：

```text
experiments/photoshop_2026/02_add_cup/
```

### 5.2 详细步骤

1. 打开 `添加物品.jpg`。
2. 观察桌面平面、墙面、光线方向和可放置区域。
3. 选择矩形选框工具或套索工具。
4. 在桌面右侧建立局部选区。
5. 选区应覆盖杯子预计出现的位置，并包含一小部分桌面区域，以便生成接触阴影。
6. 保存选区截图：

```text
experiments/photoshop_2026/02_add_cup/01_open_and_select_table_right.png
```

7. 点击“创成式填充”。
8. 保存填充对话截图：

```text
experiments/photoshop_2026/02_add_cup/02_generative_fill_dialog.png
```

9. 输入提示词：

```text
在桌面右侧添加一个白色陶瓷咖啡杯，真实光影，匹配原图透视
```

10. 保存提示词截图：

```text
experiments/photoshop_2026/02_add_cup/03_prompt_entered.png
```

11. 点击“生成”。
12. 保存处理中截图：

```text
experiments/photoshop_2026/02_add_cup/04_generate_clicked_processing.png
experiments/photoshop_2026/02_add_cup/04_generate_pressed_processing.png
```

13. 生成完成后查看图层面板。
14. 保存生成完成截图：

```text
experiments/photoshop_2026/02_add_cup/05_generation_complete_layers.png
```

15. 检查杯子与桌面的接触点是否自然。
16. 检查杯口、杯身椭圆透视是否与相机角度一致。
17. 检查杯子阴影是否匹配原图光源。
18. 检查生成区域是否误改桌面边缘或墙面。
19. 导出 PNG：

```text
experiments/photoshop_2026/02_add_cup/add_cup_ps2026_round1_result.png
```

20. 保存 PSD：

```text
experiments/photoshop_2026/02_add_cup/add_cup_ps2026_round1_layered.psd
```

## 6. 任务三：扩展画面

### 6.1 任务目标

扩展自然风景图像画布，补全天空、山体、湖面或地面纹理，并保持原图风格一致。

原图路径：

```text
experiments/photoshop_2026/00_originals/扩展画面.jpg
```

过程截图目录：

```text
experiments/photoshop_2026/03_expand_canvas/
```

### 6.2 详细步骤

1. 打开 `扩展画面.jpg`。
2. 选择“图像” -> “画布大小”。
3. 根据实验目标扩大画布宽度。
4. 将锚点设置在原图中心或需要保留的位置。
5. 确认画布左右或单侧出现透明区域。
6. 使用矩形选框工具框选透明区域。
7. 选区应轻微覆盖原图边缘，让模型读取山体、天空和地面的上下文。
8. 保存画布扩展和选区截图：

```text
experiments/photoshop_2026/03_expand_canvas/01_canvas_expanded_side_selection.png
```

9. 点击“创成式填充”。
10. 保存对话截图：

```text
experiments/photoshop_2026/03_expand_canvas/02_generative_fill_dialog.png
```

11. 输入提示词：

```text
补全自然风景，保持原图风格和光线一致
```

12. 保存提示词截图：

```text
experiments/photoshop_2026/03_expand_canvas/03_prompt_entered.png
```

13. 如果 Photoshop 中断或任务栏状态异常，重新打开文件并重新选择扩展区域。
14. 本仓库中断后恢复记录对应：

```text
experiments/photoshop_2026/03_expand_canvas/03_resume_state.png
experiments/photoshop_2026/03_expand_canvas/04_resume_reopen_canvas_selection.png
experiments/photoshop_2026/03_expand_canvas/05_after_click_generative_fill.png
experiments/photoshop_2026/03_expand_canvas/06_generative_fill_dialog.png
experiments/photoshop_2026/03_expand_canvas/07_reopen_and_reselect_sides.png
experiments/photoshop_2026/03_expand_canvas/08_after_click_taskbar_button.png
```

15. 再次确认提示词并点击“生成”。
16. 保存生成前后截图：

```text
experiments/photoshop_2026/03_expand_canvas/09_prompt_entered.png
experiments/photoshop_2026/03_expand_canvas/10_generate_pressed_processing.png
experiments/photoshop_2026/03_expand_canvas/11_generation_complete_layers.png
```

17. 检查山体线条是否自然延伸。
18. 检查天空色彩是否出现明显断层。
19. 检查湖面、雪线、地面纹理是否与原图边缘连续。
20. 检查扩展区域是否产生不相关物体。
21. 导出 PNG：

```text
experiments/photoshop_2026/03_expand_canvas/expand_canvas_ps2026_result.png
```

22. 保存 PSD：

```text
experiments/photoshop_2026/03_expand_canvas/expand_canvas_ps2026_layered.psd
```

## 7. 任务四：更换背景

### 7.1 任务目标

保留产品主体，将原背景替换为高级浴室或木质置物架场景，并保持产品边缘干净、阴影自然。

原图路径：

```text
experiments/photoshop_2026/00_originals/替换背景.jpg
```

过程截图目录：

```text
experiments/photoshop_2026/04_replace_background/
```

### 7.2 详细步骤

1. 打开 `替换背景.jpg`。
2. 使用“选择” -> “主体”，让 Photoshop 自动识别产品主体。
3. 检查主体选区是否覆盖完整产品。
4. 如果主体边缘漏选，可使用快速选择工具补选。
5. 保存主体选区截图：

```text
experiments/photoshop_2026/04_replace_background/02_subject_selected.png
```

6. 执行“选择” -> “反向”，将选区切换为背景区域。
7. 保存背景选区截图：

```text
experiments/photoshop_2026/04_replace_background/03_background_selected.png
```

8. 点击“创成式填充”。
9. 保存填充对话截图：

```text
experiments/photoshop_2026/04_replace_background/04_generative_fill_dialog.png
```

10. 输入提示词：

```text
将背景替换为高级浴室木质置物架场景，柔和自然光，保留产品主体
```

11. 保存提示词截图：

```text
experiments/photoshop_2026/04_replace_background/05_prompt_entered.png
```

12. 点击“生成”。
13. 保存生成处理中截图：

```text
experiments/photoshop_2026/04_replace_background/06_generate_pressed_processing.png
experiments/photoshop_2026/04_replace_background/07_generate_clicked_processing.png
```

14. 生成完成后查看整体界面：

```text
experiments/photoshop_2026/04_replace_background/08-生成的结果界面.png
```

15. 放大检查产品边缘，重点看瓶身、瓶盖、文字和透明反光区域。
16. 检查新背景是否侵入产品主体。
17. 检查光线方向是否与产品原有高光一致。
18. 检查背景材质是否符合“高级浴室木质置物架”语义。
19. 导出最终 PNG：

```text
experiments/photoshop_2026/04_replace_background/生成的结果图片.png
```

## 8. 任务五：二次编辑

### 8.1 任务目标

基于添加杯子的生成结果继续修改，验证 Photoshop 生成内容是否能进入传统后期流程。

输入文件：

```text
experiments/photoshop_2026/02_add_cup/add_cup_ps2026_round1_layered.psd
```

过程截图目录：

```text
experiments/photoshop_2026/05_second_round/
```

### 8.2 详细步骤

1. 打开添加杯子的 PSD。
2. 在图层面板中找到杯子的生成图层。
3. 选择移动工具。
4. 轻微移动杯子生成图层，检查杯子位置与桌面关系。
5. 保存移动检查截图：

```text
experiments/photoshop_2026/05_second_round/01_cup_generated_layer_moved_left_check.png
```

6. 尝试添加调整图层，例如色相/饱和度。
7. 如果调整层作用范围不正确或出现错误状态，记录该状态。
8. 保存错误状态截图：

```text
experiments/photoshop_2026/05_second_round/02_adjustment_error_state.png
```

9. 重新建立调整图层。
10. 将调整图层设置为剪贴蒙版，只影响生成杯子图层。
11. 适当降低饱和度，让杯子更接近原图光影。
12. 保存剪贴调整截图：

```text
experiments/photoshop_2026/05_second_round/03_adjustment_layer_clipped_and_reduced_saturation.png
```

13. 给生成图层添加或编辑图层蒙版。
14. 使用画笔在蒙版上擦除不需要的右侧局部区域。
15. 保存蒙版编辑截图：

```text
experiments/photoshop_2026/05_second_round/04_generated_layer_mask_erased_right_part.png
```

16. 对比一次生成结果和二次编辑结果。
17. 保存对比图：

```text
experiments/photoshop_2026/05_second_round/add_cup_before_after_comparison.png
```

18. 导出最终 PNG：

```text
experiments/photoshop_2026/05_second_round/add_cup_second_round_final.png
```

19. 保存二次编辑 PSD：

```text
experiments/photoshop_2026/05_second_round/add_cup_second_round_ps2026_layered.psd
```

### 8.3 二次编辑记录要点

1. 记录是否可以移动生成图层。
2. 记录是否可以单独调整生成内容的颜色。
3. 记录蒙版是否能隐藏局部生成区域。
4. 记录二次编辑是否影响原图其他区域。
5. 这些内容是论文中突出 Photoshop 优势的重要证据，因为它说明 Photoshop 不只是“一次性生图”，而是能进入可控、可逆、可追溯的后期流程。

## 9. 千问、即梦、豆包对照步骤

对照平台不要求完全复刻 Photoshop 的图层结构，重点是保持任务语义一致，并记录最终输出尺寸、结果质量和是否可二次编辑。

### 9.1 通用对照流程

1. 打开对应平台的图像生成或图像编辑入口。
2. 上传与 Photoshop 任务相同的原图。
3. 选择局部编辑、图像编辑或扩图功能。
4. 输入与 Photoshop 组语义一致的提示词。
5. 点击生成。
6. 保存最终结果图。
7. 记录平台是否提供图层、蒙版、局部修改或再次编辑能力。
8. 记录输出图像的像素尺寸。
9. 检查是否有平台水印。
10. 将结果保存到对应目录。

### 9.2 千问结果保存路径

```text
experiments/qwen_20260512/01_delete_object/删除杂物的生成图.png
experiments/qwen_20260512/02_add_cup/增加物品生成图.png
experiments/qwen_20260512/03_expand_canvas/扩展背景的生成图.png
experiments/qwen_20260512/04_replace_background/更换背景的生成图.png
experiments/qwen_20260512/05_second_round/二次修改生成图.png
```

### 9.3 即梦结果保存路径

```text
experiments/jimeng/01_delete_object/删除物品的生成结果.png
experiments/jimeng/02_add_cup/增加物品的生成结果图.png
experiments/jimeng/03_expand_canvas/扩充图片生成结果图.png
experiments/jimeng/04_replace_background/更换背景生成图片.png
experiments/jimeng/05_second_round/二次修改生成图.png
```

### 9.4 豆包结果保存路径

```text
experiments/doubao/01_delete_object/删除杂物的生成结果.png
experiments/doubao/02_add_cup/增加物品的生图结果.png
experiments/doubao/03_expand_canvas/扩展背景的生图结果.png
experiments/doubao/04_replace_background/更换背景的生图结果.png
experiments/doubao/05_second_round/二次编辑生成图片.png
```

豆包界面记录：

```text
experiments/doubao/操作界面.png
experiments/doubao/01_delete_object/删除杂物的豆包模型选择和提示词输入.png
```

## 10. 结果检查清单

每完成一个任务，按以下清单检查：

| 检查项 | 说明 |
|---|---|
| 原图是否保留 | 原始文件不得被覆盖 |
| 选区截图是否保存 | 能看到编辑范围 |
| 提示词截图是否保存 | 能复现任务语义 |
| 处理中截图是否保存 | 能证明操作流程 |
| 生成完成截图是否保存 | 能看到图层或平台结果 |
| 最终 PNG 是否导出 | 便于论文和 README 展示 |
| PSD 是否保存 | Photoshop 组重点保留可编辑证据 |
| 输出尺寸是否记录 | 用于 `docs/RESULTS.md` 的分辨率对比 |
| 是否有水印 | 用于交付适配性分析 |
| 是否可二次编辑 | 用于证明专业工作流优势 |

## 11. 论文写作取证建议

如果后续要写论文或课程报告，建议从每个任务中提取以下证据：

1. 分辨率证据：引用 `docs/RESULTS.md` 中的输出尺寸表。
2. 局部控制证据：引用 Photoshop 选区截图和生成完成截图。
3. 可编辑性证据：引用 PSD、生成图层、蒙版、调整图层截图。
4. 二次编辑证据：引用 `05_second_round` 中移动图层、剪贴调整层和蒙版擦除截图。
5. 对照证据：引用千问、即梦、豆包最终 PNG，说明通用平台更偏一次性结果。
6. 工作流证据：说明 Photoshop 能把 AI 生成结果嵌入传统修图流程，而不是把整张图重绘成不可拆分位图。

## 12. GitHub 提交新结果

如果复现实验后新增或替换文件，按以下步骤提交：

1. 查看改动：

```bash
git status --short
```

2. 添加文件：

```bash
git add docs experiments checksums scripts README.md
```

3. 提交：

```bash
git commit -m "Add detailed step-by-step operation guide"
```

4. 推送：

```bash
git push origin main
```

5. 如果出现超过 100 MB 的文件，不要直接提交，应先拆分文件或改用 Git LFS。

