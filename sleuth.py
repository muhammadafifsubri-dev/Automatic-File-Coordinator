# sleuth(Automated File Coordinator)
# still under development
# Open-Source code developed by AfifSubri

import os
from pathlib import Path
import shutil

#source of the path
src = '.'
    
#format txt    
for path in Path('.').glob('*.txt'):
    print(path)
    shutil.move(path, "text-stuff/")
    continue
    
#format pdf    
for path in Path('.').glob('*.pdf'):
    print(path)
    shutil.move(path, "pdf-stuff/")
    continue 
    
#format jpg
for path in Path('.').glob('*.jpg'):
    shutil.move(path, "jpg-stuff/")
    continue    