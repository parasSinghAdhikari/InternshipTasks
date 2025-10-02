"""
Image Resizer Tool
Batch resize and convert images using Python and Pillow

Features:
- Resize images by scale factor, specific dimensions, or maintain aspect ratio
- Convert between different image formats (JPEG, PNG, WEBP, etc.)
- Batch process entire folders
- Preserve image quality with configurable compression
- Support for multiple input formats

Usage Examples:
    python image_resizer.py /path/to/images --scale 0.5
    python image_resizer.py /path/to/images --width 800 --format JPEG
    python image_resizer.py /path/to/images --width 1920 --height 1080 --output /path/to/output
"""

from PIL import Image
import os
from pathlib import Path

def resize_images(input_folder, output_folder=None, width=None, height=None, 
                 scale_factor=None, format_convert=None, quality=95):
    """
    Resize and convert images in batch
    
    Args:
        input_folder (str): Path to folder containing images
        output_folder (str): Path to output folder (default: input_folder/resized)
        width (int): Target width in pixels
        height (int): Target height in pixels
        scale_factor (float): Scale factor (e.g., 0.5 for 50% size)
        format_convert (str): Convert to format (JPEG, PNG, WEBP, etc.)
        quality (int): Quality for JPEG compression (1-100)
    
    Returns:
        int: Number of successfully processed images
    """
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp'}
    
    # Create input path object
    input_path = Path(input_folder)
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder '{input_folder}' not found")
    
    # Set output folder
    if output_folder is None:
        output_path = input_path / "resized"
    else:
        output_path = Path(output_folder)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get list of image files
    image_files = [f for f in input_path.iterdir() if f.is_file() and f.suffix.lower() in supported_formats]
    
    if not image_files:
        print(f"No supported image files found in '{input_folder}'")
        return 0
    
    processed_count = 0
    
    print(f"Found {len(image_files)} image(s) to process...")
    print(f"Output directory: {output_path}")
    
    for image_file in image_files:
        try:
            # Open image
            with Image.open(image_file) as img:
                original_size = img.size
                print(f"\nProcessing: {image_file.name} ({original_size[0]}x{original_size[1]})")
                
                # Determine new size
                if scale_factor:
                    new_width = int(original_size[0] * scale_factor)
                    new_height = int(original_size[1] * scale_factor)
                elif width and height:
                    new_width, new_height = width, height
                elif width:
                    # Maintain aspect ratio using width
                    aspect_ratio = original_size[1] / original_size[0]
                    new_width = width
                    new_height = int(width * aspect_ratio)
                elif height:
                    # Maintain aspect ratio using height
                    aspect_ratio = original_size[0] / original_size[1]
                    new_height = height
                    new_width = int(height * aspect_ratio)
                else:
                    # No resize specified, just convert format if needed
                    new_width, new_height = original_size
                
                # Resize image if dimensions changed
                if (new_width, new_height) != original_size:
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    resized_img = img.copy()
                
                # Determine output format and filename
                if format_convert:
                    output_format = format_convert.upper()
                    if output_format == 'JPEG':
                        output_ext = '.jpg'
                    else:
                        output_ext = f'.{format_convert.lower()}'
                    
                    output_filename = image_file.stem + output_ext
                else:
                    output_format = img.format or 'PNG'
                    output_filename = image_file.name
                
                output_file_path = output_path / output_filename
                
                # Save image
                save_kwargs = {}
                if output_format == 'JPEG':
                    # Convert RGBA to RGB for JPEG
                    if resized_img.mode in ('RGBA', 'LA', 'P'):
                        background = Image.new('RGB', resized_img.size, (255, 255, 255))
                        if resized_img.mode == 'P':
                            resized_img = resized_img.convert('RGBA')
                        background.paste(resized_img, mask=resized_img.split()[-1] if resized_img.mode == 'RGBA' else None)
                        resized_img = background
                    save_kwargs['quality'] = quality
                    save_kwargs['optimize'] = True
                
                resized_img.save(output_file_path, format=output_format, **save_kwargs)
                
                print(f"  → Saved: {output_filename} ({new_width}x{new_height})")
                processed_count += 1
                
        except Exception as e:
            print(f"  ✗ Error processing {image_file.name}: {str(e)}")
    
    print(f"\nCompleted! Processed {processed_count}/{len(image_files)} images.")
    return processed_count


def main():
    try:
        processed = resize_images(
            input_folder="D:/projects/InternshipsTasks/Image_Resiz_Task_6/images",
            output_folder=None,
            width=200,
            height=200,
            scale_factor=0.5,
            format_convert="JPEG",
            quality=95
        )
        
        if processed == 0:
            return 1
            
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

main()