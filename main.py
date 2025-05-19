from PIL import Image
import PIL
import os
import glob

files = os.listdir()

images = [file for file in files if file.endswith(('jpg', 'png'))]

print(f"These are all of the images in our current working directory {images}")

# Defining a Python user-defined exception
class Error(Exception):
    """Base class for other exceptions"""
    pass

def convert_image(image_path, image_type):
    # 1. Opening the image:
    im = Image.open(image_path)
    # 2. Converting the image to RGB colour:

    alpha = im.getchannel('A')

    im = im.convert('RGBA').convert('P', palette=Image.ADAPTIVE, colors=255)

    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

    im.paste(255, mask)

    im.info['transparency'] = 255

    # 3. Spliting the image path (to avoid the .jpg or .png being part of the image name):
    image_name = image_path.split('.')[0]
    print(f"This is the image name: {image_name}")

    # Saving the images based upon their specific type:
    if image_type == 'jpg' or image_type == 'png':
        im.save(f"{image_name}.webp", 'webp')
    else:
        # Raising an error if we didn't get a jpeg or png file type!
        raise Error
    
for image in images:
    if image.endswith('jpg'):
        convert_image(image, image_type='jpg')
    elif image.endswith('png'):
        convert_image(image, image_type='png')
    else:
        raise Error
    
[convert_image(image, image_type='jpg') if image.endswith('jpg') else
 convert_image(image, image_type='png') for image in images]
