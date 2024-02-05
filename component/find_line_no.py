import fitz  # PyMuPDF

def extract_text_from_region(pdf_path):
    # Define the rectangles and their corresponding heights
    rectangles = [
        {"x": 309.2, "y": 601, "width": 170, "height": 4},
        {"x": 309.2, "y": 606, "width": 170, "height": 6},
        {"x": 309.2, "y": 614, "width": 170, "height": 6},
        {"x": 309.2, "y": 620.5, "width": 170, "height": 6},
        {"x": 309.2, "y": 627, "width": 170, "height": 6},
        {"x": 309.2, "y": 633, "width": 170, "height": 6},
        {"x": 309.2, "y": 640, "width": 170, "height": 6},
    ]

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Select the page (assuming you want the first page, change index if needed)
    page = pdf_document[0]
    
    line_no = None

    for i, rect_info in enumerate(rectangles, start=1):
        rect = fitz.Rect(rect_info["x"], rect_info["y"], rect_info["x"] + rect_info["width"], rect_info["y"] + rect_info["height"])
        text = page.get_text("text", clip=rect)
        
        if "Address" in text:
            line_no = i
            break

    # Close the PDF document
    pdf_document.close()

    return line_no

# Example usage:
# pdf_path = "ANKI1996_decrypted.pdf"
# line_no = extract_text_from_region(pdf_path)
# print("Line number containing 'Address':", line_no)
