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
    
    # 2. Converting the image based on whether it has an alpha channel
    if 'A' in im.getbands():
        # Handle images with alpha channel (transparency)
        alpha = im.getchannel('A')
        im = im.convert('RGBA').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        im.paste(255, mask)
        im.info['transparency'] = 255
    else:
        # Handle images without alpha channel (RGB or other formats)
        im = im.convert('RGB')

    # 3. Spliting the image path (to avoid the .jpg or .png being part of the image name):
    image_name = image_path.split('.')[0]
    print(f"Converting: {image_path} -> {image_name}.webp")

    # Saving the images based upon their specific type:
    if image_type == 'jpg' or image_type == 'png':
        # For JPG images (no transparency), use quality parameter
        if image_type == 'jpg':
            im.save(f"{image_name}.webp", 'webp', quality=85)
        # For PNG images (possible transparency), maintain transparency if present
        else:
            im.save(f"{image_name}.webp", 'webp', lossless=True)
    else:
        # Raising an error if we didn't get a jpeg or png file type!
        raise Error(f"Unsupported image type: {image_type}")
    
    print(f"Successfully converted {image_path} to {image_name}.webp")
    
# Process all images in the directory
print(f"Starting conversion of {len(images)} images...")
for image in images:
    try:
        if image.endswith('jpg'):
            convert_image(image, image_type='jpg')
        elif image.endswith('png'):
            convert_image(image, image_type='png')
        else:
            print(f"Skipping {image}: not a jpg or png file")
    except Exception as e:
        print(f"Error converting {image}: {str(e)}")

print("Conversion complete!")
