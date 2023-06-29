# This is a basic code which will convert a format of an image file into another format.
# Author: Huzbi
# Date: 30/06/2023

from PIL import Image

def webp_to_png(input_path, output_path):
    try:
        im = Image.open(input_path).convert("RGB")
        im.save(output_path, "png")
        print("Conversion successful!")
    except IOError:
        print("Cannot convert the image.")

input_path = "file.webp"
output_path = "file.png"

webp_to_png(input_path, output_path)
