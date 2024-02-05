import fitz  # PyMuPDF

def capture_screenshot(pdf_path, output_image_path, x, y, width, height, dpi):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Select the page (assuming you want the first page, change index if needed)
    page = pdf_document[0]
    
    # Set the zoom factor based on DPI
    zoom_factor = dpi / 72.0
    
    # Define the rectangle to capture based on X, Y, Width, Height
    rect = fitz.Rect(x, y, x + width, y + height)
    
    # Create a pixmap for the specified region
    pixmap = page.get_pixmap(matrix=fitz.Matrix(zoom_factor, zoom_factor), clip=rect)
    
    jpg_quality = 4000
    # Save the pixmap as an image
    pixmap._writeIMG(output_image_path, "png", jpg_quality)

    # Close the PDF document
    pdf_document.close()

    return output_image_path

# Example usage:
# pdf_path = "ANKI1996_decrypted.pdf"
# output_image_path = "output_screenshot.png"

# x_position = 115  # Replace with your X-axis position
# y_position = 600  # Replace with your Y-axis position
# capture_width = 170  # Replace with the width you desire
# capture_height = 42  # Replace with the height you desire

# x_position = 309.2  # Replace with your X-axis position
# y_position = 600  # Replace with your Y-axis position
# capture_width = 150  # Replace with the width you desire
# capture_height = 30
# dpi = 1600  # Desired DPI

# capture_screenshot(pdf_path, output_image_path, x_position, y_position, capture_width, capture_height, dpi)
