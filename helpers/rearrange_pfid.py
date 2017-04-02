#Code to put images from pfid folders into tensorflow trainable folders

import os
import os.path
import shutil

folder_path = "/home/xiaozheng/meal_data/pfid"
new_folder_path = "/home/xiaozheng/meal_data/pfid_correct_format"

image_path_list = []
with open('./pfid/images.txt') as f:
    image_path_list = f.readlines()

image_path_list = [path.strip() for path in image_path_list]

for image_path in image_path_list:
    folder_name = image_path.split('/')[2]

    new_path = os.path.join(new_folder_path, folder_name)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    old_image_path = folder_path + image_path[1:]
    new_image_path = os.path.join(new_path, image_path.split('/')[-1])
    if os.path.exists(old_image_path):
        shutil.copy(old_image_path, new_image_path)
