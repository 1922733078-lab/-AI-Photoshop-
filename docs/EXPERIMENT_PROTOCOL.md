# 完整实验操作流程

## 1. 实验概述

本实验围绕 Photoshop 2026 创成式填充功能展开，主要考察其在城市视觉图像编辑和专业后期工作流中的适用性。实验采用同一批样品图，在 Photoshop 2026、千问、即梦、豆包四类工具中完成相似编辑任务，并保存过程截图、最终结果和可编辑文件。

实验日期：2026 年 5 月 12 日。  
实验产出目录：`experiments/`。

## 2. 实验样品

样品图位于：

```text
experiments/samples/
```

样品包括：

| 文件 | 用途 |
|---|---|
| 删除杂物.jpg | 删除街景画面中的垃圾桶或杂物 |
| 添加物品.jpg | 在桌面场景中添加杯子 |
| 扩展画面.jpg | 横向扩展自然风景画面 |
| 替换背景.jpg | 替换产品图背景 |
| 删除路人备用.jpg | 备用人像／街景移除任务 |
| 删除电线备用.jpg | 备用复杂线条移除任务 |

## 3. 实验工具

### 3.1 Photoshop 2026

Photoshop 2026 组保存了完整操作截图、最终 PNG 结果和 PSD 分层文件。创成式填充模型选择界面见：

```text
experiments/photoshop_2026/创成式填充功能内置的AI生图模型.png
```

该界面记录了 Photoshop 2026 中可选择的 Adobe Firefly、FLUX、Gemini 等图像生成或图像编辑模型。本实验重点关注模型生成结果进入 Photoshop 图层、蒙版、调整图层后的可编辑工作流。

### 3.2 对照工具

对照平台包括：

- 千问生图：`experiments/qwen_20260512/`
- 即梦图片生成：`experiments/jimeng/`
- 豆包生图：`experiments/doubao/`

这些平台主要保存最终生成结果，部分平台保存界面截图。

## 4. Photoshop 2026 操作流程

### 4.1 任务一：删除杂物

目标：删除街景图像中的垃圾桶，并补全地面、阴影和背景。

原图：

```text
experiments/photoshop_2026/00_originals/删除杂物.jpg
```

操作步骤：

1. 使用 Photoshop 2026 打开 `删除杂物.jpg`。
2. 使用矩形选框工具框选垃圾桶及其周边区域。
3. 点击上下文任务栏中的“创成式填充”。
4. 输入提示词：`删除画面中的垃圾桶，并自然补全背景，保持光影和透视一致`。
5. 点击“生成”，等待生成图层返回。
6. 检查图层面板，确认结果保存在生成图层中。
7. 导出最终 PNG，并保存 PSD 分层文件。

过程截图：

```text
experiments/photoshop_2026/01_delete_object/01_open_and_select_garbage.png
experiments/photoshop_2026/01_delete_object/02_generative_fill_dialog.png
experiments/photoshop_2026/01_delete_object/03_prompt_entered_cgevent.png
experiments/photoshop_2026/01_delete_object/03_prompt_entered_manual_check.png
experiments/photoshop_2026/01_delete_object/04_generate_clicked_empty_prompt.png
experiments/photoshop_2026/01_delete_object/04_generate_clicked_processing.png
experiments/photoshop_2026/01_delete_object/05_generate_pressed_return.png
experiments/photoshop_2026/01_delete_object/06_generation_complete_layers.png
experiments/photoshop_2026/01_delete_object/07_generated_layer_hidden_original_restored.png
```

最终结果：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_result.png
```

PSD 分层文件：

```text
experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd
```

注意：该 PSD 在仓库中以分卷保存，需执行 `scripts/reconstruct_large_files.sh` 后还原。

### 4.2 任务二：添加物品

目标：在桌面右侧添加一个白色陶瓷咖啡杯，并保持原图透视和真实光影。

原图：

```text
experiments/photoshop_2026/00_originals/添加物品.jpg
```

操作步骤：

1. 打开 `添加物品.jpg`。
2. 在桌面右侧建立局部选区。
3. 调用“创成式填充”。
4. 输入提示词：`在桌面右侧添加一个白色陶瓷咖啡杯，真实光影，匹配原图透视`。
5. 点击“生成”。
6. 检查杯子与桌面边缘、墙面纹理和场景光影的融合关系。
7. 导出 PNG，并保存 PSD 分层文件。

过程截图：

```text
experiments/photoshop_2026/02_add_cup/01_open_and_select_table_right.png
experiments/photoshop_2026/02_add_cup/02_generative_fill_dialog.png
experiments/photoshop_2026/02_add_cup/03_prompt_entered.png
experiments/photoshop_2026/02_add_cup/04_generate_clicked_processing.png
experiments/photoshop_2026/02_add_cup/04_generate_pressed_processing.png
experiments/photoshop_2026/02_add_cup/05_generation_complete_layers.png
```

最终结果：

```text
experiments/photoshop_2026/02_add_cup/add_cup_ps2026_round1_result.png
experiments/photoshop_2026/02_add_cup/add_cup_ps2026_round1_layered.psd
```

### 4.3 任务三：扩展画面

目标：扩展自然风景图像画布，补全山体、天空和地面纹理。

原图：

```text
experiments/photoshop_2026/00_originals/扩展画面.jpg
```

操作步骤：

1. 打开 `扩展画面.jpg`。
2. 扩展画布，使图像左右或单侧出现透明区域。
3. 框选透明区域及相邻边缘区域。
4. 调用“创成式填充”。
5. 输入提示词：`补全自然风景，保持原图风格和光线一致`。
6. 点击“生成”。
7. 检查山体边缘、天空色彩、雪线和湖面反射是否连续。
8. 导出最终 PNG，并保存 PSD 分层文件。

过程截图：

```text
experiments/photoshop_2026/03_expand_canvas/01_canvas_expanded_side_selection.png
experiments/photoshop_2026/03_expand_canvas/02_generative_fill_dialog.png
experiments/photoshop_2026/03_expand_canvas/03_prompt_entered.png
experiments/photoshop_2026/03_expand_canvas/04_resume_reopen_canvas_selection.png
experiments/photoshop_2026/03_expand_canvas/05_after_click_generative_fill.png
experiments/photoshop_2026/03_expand_canvas/06_generative_fill_dialog.png
experiments/photoshop_2026/03_expand_canvas/07_reopen_and_reselect_sides.png
experiments/photoshop_2026/03_expand_canvas/09_prompt_entered.png
experiments/photoshop_2026/03_expand_canvas/10_generate_pressed_processing.png
experiments/photoshop_2026/03_expand_canvas/11_generation_complete_layers.png
```

最终结果：

```text
experiments/photoshop_2026/03_expand_canvas/expand_canvas_ps2026_result.png
experiments/photoshop_2026/03_expand_canvas/expand_canvas_ps2026_layered.psd
```

### 4.4 任务四：更换背景

目标：保留产品主体，替换为高级浴室或木质置物架场景。

原图：

```text
experiments/photoshop_2026/00_originals/替换背景.jpg
```

操作步骤：

1. 打开 `替换背景.jpg`。
2. 使用“选择主体”功能识别产品主体。
3. 反选背景区域。
4. 调用“创成式填充”。
5. 输入提示词：`将背景替换为高级浴室木质置物架场景，柔和自然光，保留产品主体`。
6. 点击“生成”。
7. 检查产品边缘、阴影、背景材质和光照方向。
8. 导出最终 PNG。

过程截图：

```text
experiments/photoshop_2026/04_replace_background/01_open_original.png
experiments/photoshop_2026/04_replace_background/02_subject_selected.png
experiments/photoshop_2026/04_replace_background/03_background_selected.png
experiments/photoshop_2026/04_replace_background/04_generative_fill_dialog.png
experiments/photoshop_2026/04_replace_background/05_prompt_entered.png
experiments/photoshop_2026/04_replace_background/06_generate_pressed_processing.png
experiments/photoshop_2026/04_replace_background/07_generate_clicked_processing.png
experiments/photoshop_2026/04_replace_background/08-生成的结果界面.png
```

最终结果：

```text
experiments/photoshop_2026/04_replace_background/生成的结果图片.png
```

### 4.5 任务五：二次编辑

目标：对已生成杯子结果继续进行位置、饱和度和局部遮罩调整。

操作步骤：

1. 打开添加杯子的 PSD 或结果图。
2. 移动生成图层，检查杯子位置与桌面关系。
3. 尝试创建调整层；若出现调整错误，重新建立剪贴调整层。
4. 降低杯子或局部区域饱和度，使其更接近原图光影。
5. 使用图层蒙版擦除不需要的右侧局部区域。
6. 导出最终结果并保存二次编辑 PSD。

过程截图：

```text
experiments/photoshop_2026/05_second_round/01_cup_generated_layer_moved_left_check.png
experiments/photoshop_2026/05_second_round/02_adjustment_error_state.png
experiments/photoshop_2026/05_second_round/03_adjustment_layer_clipped_and_reduced_saturation.png
experiments/photoshop_2026/05_second_round/04_generated_layer_mask_erased_right_part.png
```

最终结果：

```text
experiments/photoshop_2026/05_second_round/add_cup_second_round_final.png
experiments/photoshop_2026/05_second_round/add_cup_second_round_ps2026_layered.psd
```

## 5. 对照平台操作流程

千问、即梦、豆包平台均采用与 Photoshop 组语义一致的任务目标进行编辑。由于不同平台的界面和模型版本不同，本仓库主要保存最终图像结果和部分界面截图，不假定其后台模型完全一致。

### 5.1 千问生图

结果目录：

```text
experiments/qwen_20260512/
```

任务结果：

```text
01_delete_object/删除杂物的生成图.png
02_add_cup/增加物品生成图.png
03_expand_canvas/扩展背景的生成图.png
04_replace_background/更换背景的生成图.png
05_second_round/二次修改生成图.png
```

### 5.2 即梦图片生成

结果目录：

```text
experiments/jimeng/
```

任务结果：

```text
01_delete_object/删除物品的生成结果.png
02_add_cup/增加物品的生成结果图.png
03_expand_canvas/扩充图片生成结果图.png
04_replace_background/更换背景生成图片.png
05_second_round/二次修改生成图.png
```

### 5.3 豆包生图

结果目录：

```text
experiments/doubao/
```

任务结果：

```text
01_delete_object/删除杂物的生成结果.png
02_add_cup/增加物品的生图结果.png
03_expand_canvas/扩展背景的生图结果.png
04_replace_background/更换背景的生图结果.png
05_second_round/二次编辑生成图片.png
```

豆包平台保存了额外界面截图：

```text
experiments/doubao/操作界面.png
experiments/doubao/01_delete_object/删除杂物的豆包模型选择和提示词输入.png
```

## 6. 评价指标

本实验采用以下指标进行对照：

| 指标 | 记录方式 | 解释 |
|---|---|---|
| 输出尺寸 | 读取 PNG/JPG 像素尺寸 | 衡量是否适合后续高分辨率编辑 |
| 相对像素比例 | 输出像素数 / 原图像素数 | 衡量分辨率保持或扩展程度 |
| PSD 分层文件 | 是否存在 PSD | 衡量是否保留专业后期可编辑空间 |
| 过程截图 | 是否保存中间步骤 | 衡量实验可追溯性 |
| 水印情况 | 最终图是否带平台水印 | 衡量公开展示或交付便利性 |
| 二次编辑稳定性 | 是否能基于图层和蒙版继续修改 | 衡量是否适合多轮修图 |

## 7. 复现实验注意事项

1. 生成式图像平台的模型版本可能随时间更新，因此重新生成结果可能与本仓库结果不同。
2. 本仓库保存的是 2026 年 5 月 12 日实验过程中的具体输出。
3. Photoshop 组保留了更多操作截图和 PSD 文件，因此更适合分析工作流可追溯性。
4. 对照平台主要保留最终位图结果，因此更适合分析一次性生成输出。
