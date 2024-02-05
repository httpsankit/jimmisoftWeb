"""
Copyright (c) 2022-2023.  Ehatech Pvt Ltd - All Rights Reserved.
"""

"""
Created on 23-May-2023

@author: shankarkumar
"""
import fitz
import logging
from box import Box
from PIL import Image

from jimmisoft import product_setting


def get_prd_setting(db_name=None):
    """
    Retrieves the product setting object.

    Args:
        db_name (str, optional): Database name. Defaults to None.

    Returns:
        Box: Product setting object.
    """
    if db_name:
        # TODO: Implement database product setting retrieval
        pass
    else:
        prd_setting_dict = product_setting.prd_setting_dict
        prd_setting_obj = Box(prd_setting_dict)

    return prd_setting_obj

def generate_log_config():
    """
        Logger function for all file
            
        Returns:
            return the Logger configuration
    """
    logger = logging
    logger.basicConfig(filename=product_setting.log_file_path, level=product_setting.log_level,format='%(asctime)s - %(levelname)s - %(message)s')
    return logger

def get_total_cost(file_path,balance):
    """
    This function calculate total cost on many pages file like pdf

    arg:-
    file_path:- taking file path from local
    balance:- balance is taking from product setting according to function

    return :-
    Total cost on each file
    
    """
    pdf = fitz.open(file_path)
    page_count = pdf.page_count
    pdf.close()
    total_cost = page_count*balance
    # data = {
    #         "total_cost":total_cost,
    #         "total_page":page_count
    #         }
    return total_cost, page_count