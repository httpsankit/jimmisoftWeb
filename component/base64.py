import base64
# from PIL import Image

def image_to_base64(image_path):
    try:
        # Open the image file
        with open(image_path, "rb") as image_file:
            # Read the image file content
            image_content = image_file.read()
            
            # Encode the image content to base64
            base64_encoded = base64.b64encode(image_content).decode('utf-8')
            
            return base64_encoded

    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

# Example usage:
# image_path = "path/to/your/image.jpg"
# base64_data = image_to_base64(image_path)

# if base64_data:
#     print("Base64 encoded image:", base64_data[:50])  # Print the first 50 characters for demonstration
