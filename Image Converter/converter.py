# This is a basic code which will convert a format of an image file into another format.
# Author: Huzbi
# Date: 30/06/2023
# Last Update: 30/06/2023 3:27PM PST

from PIL import Image
import os

def webp_to_img(input_path):
    print("To PNG or JPEG? Enter in small caps.")
    ft_type = input()
    if (ft_type == "png"):
        for filename in os.listdir(input_path):
            if filename.endswith('.webp'):
                file_path = os.path.join(input_path, filename)
                im = Image.open(file_path).convert("RGB")
                new_file_path = os.path.splitext(file_path)[0] + '.png'
                im.save(new_file_path, "png")
                print("Conversion successful!")
    elif (ft_type == "jpeg" or ft_type == "jpg"):
        for filename in os.listdir(input_path):
            if filename.endswith('.webp'):
                file_path = os.path.join(input_path, filename)
                im = Image.open(file_path).convert("RGB")
                new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                im.save(new_file_path, "jpeg")
                print("Conversion Successful!")
    else:
        print("Error: Conversion Unsuccessful.")

script_directory = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_directory, "webp_files")

webp_to_img(input_path)
