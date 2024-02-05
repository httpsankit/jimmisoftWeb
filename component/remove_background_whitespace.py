from PIL import Image, ImageOps

def remove_background_and_whitespace(image_path, output_path, bg_tolerance=20):
    """Removes both whitespace and white background from an image and saves it as a PNG with transparency.

        image_path (str): Path to the image file.
        bg_tolerance (int, optional): Threshold for considering pixels as part of the white background. Defaults to 20.
    """

    img = Image.open(image_path).convert("RGBA")

    # Remove whitespace using grayscale bounding box
    img_gray = img.convert('L')
    bbox = ImageOps.invert(img_gray).getbbox()

    if bbox:
        img = img.crop(bbox)  # Crop image to bounding box

    # Remove white background based on tolerance
    datas = img.getdata()
    newData = []
    for item in datas:
        if (
            abs(item[0] - 255) <= bg_tolerance
            and abs(item[1] - 255) <= bg_tolerance
            and abs(item[2] - 255) <= bg_tolerance
        ):
            newData.append((item[0], item[1], item[2], 0))  # Make white transparent
        else:
            newData.append(item)

    img.putdata(newData)

    # Save as PNG with transparency
    
    img.save(output_path, format="PNG")

    return output_path


# Example usage
# image_path = "output_screenshot.png"  # Replace with your image path
# remove_background_and_whitespace(image_path, output_path)
