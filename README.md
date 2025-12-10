# AI Humanizer / AI 文本人性化

[English Setup](#english) | [中文说明](#chinese)

---

<a name="english"></a>
## English Description

**AI Humanizer** is a lightweight text processing tool designed to introduce subtle "human-like" imperfections into text.

### Key Features
- **Perturbation Magic**: Introduces random variations to make text appear less machine-generated.
- **Smart Formatting**: Automatically handles paragraph spacing.
- **Double Magic**: Apply recursive processing for stronger effects.

### Note on BERT Removal
Previously, this project utilized the **BERT** model for synonym replacement. However, it was observed that BERT caused **excessive perturbation**, often altering the original meaning or making the text sound unnatural. Therefore, the BERT model has been **completely removed**. The tool now uses a tuned algorithm ensuring:
- **Capitalization Variations** (~15% chance).
- **Random Spacing** to break AI detection patterns.

### Installation & Usage

1. **Requirements**:
   - Python 3.x
   - PyQt6

   ```bash
   pip install PyQt6
   ```

2. **Run the application**:
   ```bash
   python ai文本人性化.py
   ```

---

<a name="chinese"></a>
## 中文说明

**AI 文本人性化 (AI Humanizer)** 是一个轻量级的文本处理工具，旨在通过引入细微的“人性化”瑕疵，让文本看起来更像是人类书写的。

### 主要功能
- **文本魔法**: 引入随机变化，使文本看起来不那么像机器生成的。
- **智能格式化**: 自动处理段落间距。
- **双重魔法**: 进行递归处理以获得更强的效果。

### 关于移除 BERT 模型的说明
本项目最初使用 **BERT** 模型进行同义词替换。然而，经过测试发现，BERT 造成的**扰动过大 (excessive perturbation)**，往往会改变原本的含义或使文本读起来不自然。因此，我们**彻底移除了 BERT 模型**，转而使用微调后的算法，专注于：
- **大小写变化**: 约 15% 的概率。
- **随机空格**: 打破 AI 检测模式。

### 安装与使用

1. **环境要求**:
   - Python 3.x
   - PyQt6

   ```bash
   pip install PyQt6
   ```

2. **运行程序**:
   ```bash
   python ai文本人性化.py
   ```
