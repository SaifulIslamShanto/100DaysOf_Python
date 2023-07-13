# 1. pillow library
# pip install pillow

# 2. Rembg Library
# pip install rembg

# 3. Easygui Library
# pip install easygui

from rembg import remove
from PIL import Image
import easygui


print("Please Wait")
input_path = easygui.fileopenbox("Select your Image")
output_path = easygui.filesavebox("Where you want to save your image")

my_img = Image.open(input_path)
print("Please Wait")
rem = remove(my_img)

save = rem.save(output_path)
print("Successfully Done, Check Your Folder")
