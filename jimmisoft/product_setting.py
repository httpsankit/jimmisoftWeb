import os
import logging

# from dotenv import load_dotenv
data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")
google_credentials_path =  os.path.join(data_folder, "config_files/key.json")
google_drive_credentials_path =  os.path.join(data_folder, "config_files/credentials.json")
log_file_path = os.path.join(data_folder, "log_files", "Expedichat.log")
image_files = 'path/to/output/directory'
document_files = 'path/to/output/documents'
audio_files = "path/to/output/directory"
model_flag = False
log_level = logging.ERROR

ocr_free_flag = True


prd_setting_dict = {
    "data_folder": data_folder,
    "image_files": os.path.join(data_folder, "image_files"),
    "summarized_pdf": os.path.join(data_folder, "summarized_pdf"),
    "native_pdf":  os.path.join(data_folder, "native_pdf"),
    "audio_files": os.path.join(data_folder, "audio_files"),
    "document_files": os.path.join(data_folder, "documents"),
    "google_credentials_path": os.path.join(data_folder, "config_files/key.json"),
    "google_drive_credentials_path": os.path.join(data_folder, "config_files/credentials.json"),
    "native_text_extractor_credit": 2,
    "vision_ocr_credit":1,
    "scanned_pdf_text_credits":1,
    "summarizer_credits":1,
    "summarizer_credits_with_text":1,
    "ppt_generator":3,
    "daily_credits":5,
    "file_upload_credits":1,
    "resume_credits":1,
    "signup_bonous":50,
    "base64_or_imageid":True
}