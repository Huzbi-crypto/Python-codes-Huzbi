# This is a basic code which will convert a format of an image file into another format.
# Author: Huzbi
# Date Created: 30/06/2023
# Latest Update: 30/06/2023
from PIL import Image

def webp_to_img(input_path):
    print("To PNG or JPEG? Enter in small caps.")
    ft_type = input()
    if (ft_type == "png"):
        try:
            im = Image.open(input_path).convert("RGB")
            output_path = "file.png"
            im.save(output_path, "png")
            print("Conversion successful!")
        except IOError:
            print("Cannot convert the image.")
    elif (ft_type == "jpeg" or ft_type == "jpg"):
        try:
            im = Image.open(input_path).convert("RGB")
            output_path = "file.jpeg"
            im.save(output_path, "jpeg")
            print("Conversion successful!")
        except IOError:
            print("Cannot convert the image.")

input_path = "file.webp"

webp_to_img(input_path)
