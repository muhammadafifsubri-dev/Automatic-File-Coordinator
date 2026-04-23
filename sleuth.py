import os
from pathlib import Path
import shutil

src = '.'
for path in Path(src).rglob('*.py'):
    shutil.move(path, "python-stuff/")
    break