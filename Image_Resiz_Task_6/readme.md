# Image Resizer Tool
A Python script to batch resize and convert images using the Pillow library.

## Features
Resize images by scale factor, specific width and height, or maintain aspect ratio automatically

Convert images between formats like JPEG, PNG, WEBP, etc.

Batch process all supported image files in a folder

Preserve image quality with configurable compression for JPEG

Supports multiple input image formats including JPG, PNG, BMP, TIFF, and WEBP

Automatically creates an output folder if none specified, defaulting to resized inside the input folder

## Requirements
Pillow (Python Imaging Library fork)

Install Pillow with:


pip install Pillow
Usage
Run the script with parameters to specify resizing options:

python image_resizer.py /path/to/images [--width WIDTH] [--height HEIGHT] [--scale SCALE_FACTOR] [--format FORMAT] [--output OUTPUT_FOLDER] [--quality QUALITY]

## Parameters
input_folder (mandatory): Path to the folder containing images to process

--width: Target width in pixels (maintains aspect ratio if height not specified)

--height: Target height in pixels (maintains aspect ratio if width not specified)

--scale: Scale factor for resizing (e.g. 0.5 to reduce dimensions by half)

--format: Convert images to this format (e.g., JPEG, PNG)

--output: Folder to save resized images (default is a subfolder named resized inside input folder)

--quality: JPEG compression quality (1-100, default 95)

## Examples
Resize all images to 50% size:

python image_resizer.py /path/to/images --scale 0.5
Resize all images to a width of 800px, maintaining aspect ratio:

python image_resizer.py /path/to/images --width 800
Resize to 1920x1080 and convert all images to JPEG format:

python image_resizer.py /path/to/images --width 1920 --height 1080 --format JPEG
Specify output folder and JPEG quality:

python image_resizer.py /path/to/images --width 1024 --format JPEG --output /path/to/output --quality 90

## Supported Input Formats
JPG, JPEG

PNG

BMP

TIFF, TIF

WEBP

## Notes
If both width and height are specified, the image is resized exactly to those dimensions.

If only one dimension is specified, the other is adjusted to maintain the original aspect ratio.

The tool handles transparency when converting to JPEG by adding a white background.

If no resize option is specified, the script will only convert the image format if requested.

## Error Handling
Prints error messages for files it cannot process but continues with other images.

If no images are found in the input folder, it notifies and exits without error.
