import fitz  # PyMuPDF library
import os


def extract_image_from_pdf(pdf_file_path, output_path):
    # PDF file path
    # pdf_file_path = "ANKI1996_decrypted.pdf"

    # Get the PDF filename without extension
    # pdf_filename = os.path.splitext(os.path.basename(pdf_file_path))[0]

    # Create output directory for images, named after the PDF
    # pdf_filename = f"adhar_{adno}"
    # output_path = os.path.join("extracted/images", pdf_filename)
    os.makedirs(output_path, exist_ok=True)  # Create if it doesn't exist

    # Open the PDF document
    with fitz.open(pdf_file_path) as doc:
        for page_index in range(len(doc)):
            page = doc.load_page(page_index)
            images = page.get_images()

            for image_index, img in enumerate(images):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # Generate unique filename within the PDF-named folder
                image_filename = f"image_{page_index+1}_{image_index}.png"
                image_filepath = os.path.join(output_path, image_filename)

                if os.path.exists(image_filepath):
                    # Handle existing filenames if needed
                    base, ext = os.path.splitext(image_filename)
                    i = 1
                    while os.path.exists(image_filepath):
                        image_filename = f"{base}_{i}{ext}"
                        image_filepath = os.path.join(output_path, image_filename)
                        i += 1

                pix.save(image_filepath)
    return output_path
    # print(f"Images extracted successfully into the '{output_path}' folder!")