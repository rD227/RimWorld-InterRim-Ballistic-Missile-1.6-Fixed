[English](README.md)
安装说明
直接安装：

```PowerShell
pip install Pillow
```
使用虚拟环境安装（推荐，保持系统环境整洁）：

```Bash
# 1. 创建虚拟环境
python -m venv .venv

# 2. 激活虚拟环境
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

# 3. 安装依赖
pip install Pillow
```
使用方法
快速上手
将 fix_textures.py 脚本放置在模组的根目录（或者 Textures 文件夹）下，然后在该目录下运行命令：

PowerShell
python fix_textures.py
脚本会自动扫描当前文件夹下所有的 .dds 文件，并将其转换为 .png 格式。

进阶用法（指定路径）
你也可以将模组文件夹的路径作为参数传递给脚本。该脚本支持同时处理多个路径：
```powershell
python fix_textures.py "路径/到/模组A" "路径/到/模组B"
```
