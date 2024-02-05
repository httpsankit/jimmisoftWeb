"""
Copyright (c) 2022-2023.  Ehatech Pvt Ltd - All Rights Reserved.
"""

"""
Created on 10-May-2023

@author: shankarkumar
"""
import os
import re
# import logging
from box import Box
from django.core.files.storage import default_storage

# from expeditextchat import product_setting
# from utils import common_util_functions as cuf

def get_cleaned_file_name(file_name):
    """
    Generates an uploaded file name based on the given file name string.

    The function processes the file name string by removing special characters,
    splitting it into individual words, and concatenating them with underscores.
    If the resulting file name is empty, it appends 'test' to the file name.

    Args:
        file_name (str): The original file name string.

    Returns:
        str: The processed uploaded file name.
    """
    try:
        # logging.info("Uploade file name is  {}".format(file_name))
        # Extract the file extension
        period_index = file_name.rfind('.')
        if period_index != -1:
            file_extension = file_name[period_index:].lower()
            file_name = file_name[:period_index]
        else:
            file_extension = ''

        # Process and sanitize the file name
        file_name_tokens = file_name.split()
        processed_words = []
        regex = re.compile('[^a-zA-Z0-9-_]')
        for word in file_name_tokens:
            if "'s" in word:
                word = word.replace("'s", "")
            word = regex.sub('', word)
            if word:
                processed_words.append(word)

        # Generate the uploaded file name
        if processed_words:
            uploaded_file_name = "_".join(processed_words) + file_extension
        else:
            uploaded_file_name = "test" + file_extension

        # logging.info("Cleaned file name is {}".format(uploaded_file_name))
        return uploaded_file_name
    except Exception as error:
        # logging.error("get_cleaned_file_name error {}".format(error))
        return file_name

def save_file_based_on_extension(prd_setting, uploaded_file):
    """
    Saves the uploaded file to the appropriate folder based on the file type.

    The function determines the file type by checking the file extension and
    saves the file in the corresponding folder (docs, audio, or video) within
    the specified product setting data folder.

    Args:
        prd_setting (object): The product setting object.
        uploaded_file (object): The uploaded file object.
        

    Returns:
        str: The path of the saved file.
    """
    try:
        uploaded_file_name = get_cleaned_file_name(uploaded_file.name)

        file_extension = os.path.splitext(uploaded_file_name)[1].lower()
        
        # logging.info("Uploaded file extension is {}".format(file_extension))
        data_folder = prd_setting.data_folder
        
        
        if file_extension in ['.pdf', '.doc', '.docx', '.txt' ,'.ppt', '.pptx']:
            folder = 'documents'
        elif file_extension in ['.mp3', '.wav', '.aac']:
            folder = 'audio_files'
        elif file_extension in ['.mp4', '.mov', '.avi']:
            folder = 'video_files'
        elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            folder = 'image_files'
        else:
            folder = 'other'

        # Create the folder if it doesn't exist
        folder_path = os.path.join(data_folder, folder)
        # logging.info("Uploaded file folder path is {}".format(folder_path))
        os.makedirs(folder_path, exist_ok=True)

        # Save the file in the appropriate folder
        uploaded_file_path = os.path.join(folder_path, uploaded_file_name)
        saved_file_path = default_storage.save(uploaded_file_path, uploaded_file)
        
        return saved_file_path
    except Exception as error:
        # logging.error("save_file_based_on_extension error {}".format(error))
        return None

def get_file_name_without_extension(file_path):
    
    """
    Retrieves the file name without the extension from a file path.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The file name without the extension.
    """
    file_name_with_extension = os.path.basename(file_path)
    file_name = os.path.splitext(file_name_with_extension)[0]
    return file_name
