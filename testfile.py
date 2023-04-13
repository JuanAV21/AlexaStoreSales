import os
from pathlib import Path

full_path = os.getcwd()
print(str(Path(full_path).parents[0])) # "path/to"
print(str(Path(full_path).parents[1])) # "path"
print(str(Path(full_path).parents[2]))
var = os.path.dirname(os.getcwd())
print("this is the output: ", var)
print(os.getcwd())