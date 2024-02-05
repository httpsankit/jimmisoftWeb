import fitz
import uuid
import math
import logging

# from file_utils import common_util_fuctions as cuf

#Log Configuration
# logging = cuf.generate_log_config()

def extract_text_with_coordinates(file_path):
    try:
        """
        Get the text with metaData (Co-ordination).

        Arguments:
            file_path: Native pdf file path.
    
        Returns:
            A list of dictionaries containing the coordinates of the different words present on each page of the PDF.
        """
        line_no = 1
        # Opening the PDF file
        doc = fitz.open(file_path)

        # Creating an empty dictionary to store different lists
        result = {}
        page_number = 1

        # Iterate through the doc for different words
        for page in doc:
            words = page.get_text("words")
            logging.info("Pdf page number {} processing started".format(page_number))

            # Creating an empty list
            page_data = []
            for word in words:
                text = word[4]  # Extract the text
                x1, y1, x2, y2 = word[:4]  # Extract the coordinates
                width = x2 - x1
                height = y2 - y1
                confidence = word[5] if len(word) > 5 else None
                original_text = word[6] if len(word) > 6 else None
                text_type = word[7] if len(word) > 7 else None
                word_data = {
                    'text': text,
                    'x1': math.ceil(x1),
                    'y1': math.ceil(y1),
                    'x2': math.ceil(x2),
                    'y2': math.ceil(y2),
                    'width': math.ceil(width),
                    'height': math.ceil(height),
                    'confidence': confidence,
                    'original_text': original_text,
                    'text_type': text_type,
                    'Id': str(uuid.uuid4()),  # Generate unique ID for the word
                    'line_number': word[8] if len(word) > 8 else "None"  # Line number if available
                }
                page_data.append(word_data)
            result[f'page_{page_number}'] = page_data
            # logging.info("Pdf page number {} processing end".format(page_number))
            page_number += 1
        # data_processing_res = data_processing.get_all_page_text(result)
        return result

    except Exception as error:
        # logging.error("extract_text_with_coordinates error {}".format(error))
        return None