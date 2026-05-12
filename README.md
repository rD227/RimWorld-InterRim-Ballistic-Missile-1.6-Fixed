How to use:
```powershell
pip install Pillow
```
Using a Virtual Environment (Recommended):
```powershell&&bash
# 1. create the enviriment
python -m venv .venv

# 2. enable
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

# 3. install
pip install Pillow
```
二
quick use:
Place fix_textures.py in the root directory of the module (or in the Textures folder), and then run the command in that directory:
```powershell
python fix_textures.py
```
It will automatically scan all .dds in the current folder and replace them with .png in place.

Specify path usage: You can also pass the path of the module folder as a parameter to the script. Multiple paths can be passed in at the same time:
```powershell
python fix_textures.py "path/to/A" "path/to/B"
```
