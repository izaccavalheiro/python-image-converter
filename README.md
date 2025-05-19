# Image to WebP Converter

A simple Python utility that automatically converts JPG and PNG images in the current directory to WebP format.

## Description

This script scans the current working directory for JPG and PNG image files and converts them to the more efficient WebP format. WebP offers superior compression with similar or better quality compared to traditional image formats, making it ideal for web applications and reducing storage requirements.

## Features

- Automatically detects all JPG and PNG files in the current directory
- Preserves transparency in PNG images
- Maintains image quality during conversion
- Simple to use with no command-line arguments needed

## Requirements

- Python 3.x
- Pillow (PIL Fork) library

## Installation

1. Ensure you have Python 3.x installed
2. Install the required package:

```bash
pip install Pillow
```

## Usage

1. Place the script in the directory containing the images you want to convert
2. Run the script:

```bash
python image_converter.py
```

The script will:
1. List all JPG and PNG files found in the directory
2. Convert each image to WebP format
3. Save the new WebP files in the same directory with the original filename but with the .webp extension

## How It Works

1. The script identifies all JPG and PNG files in the current directory
2. For each image:
   - Opens the image using PIL
   - Handles transparency for PNG images
   - Converts the image to WebP format
   - Saves the converted image with the same base filename but with a .webp extension

## Error Handling

The script implements basic error handling:
- A custom `Error` class for exception handling
- Validation to ensure only supported image types (JPG and PNG) are processed

## Notes

- Original files are preserved during conversion
- There is a redundant conversion at the end of the script using list comprehension that duplicates the functionality of the preceding for loop
