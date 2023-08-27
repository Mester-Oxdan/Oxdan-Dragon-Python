import imports.own.start_start
import os

files_dir = os.path.dirname(__file__)
os.environ["OXDAN-DRAGON-PYTHON"] = files_dir 

#path_to_png = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"..","IMAGES","ALL","icon.png")

imports.own.start_start.start_start()
