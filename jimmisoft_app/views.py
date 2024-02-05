from django.shortcuts import render
import PyPDF2
import uuid
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from file_utils.file_utile_functions import save_file_based_on_extension
from rest_framework import status as http_status
from rest_framework import status
from text_extractor.native_text_extractor import extract_text_with_coordinates
from file_utils import common_util_fuctions as cuf
from component import extract_image, base64, find_line_no, screenshot, remove_background_whitespace,makeJson

# def hello_django(request):
#     return JsonResponse({"message": "Hi, this is a Django app"})

@api_view(['GET'])
def get_app(request):
    """
    This function help us to find out server Live or not

    Returns:
        return the msg :- "msg": "this is your Expeditext app"
    """
    try:
        return JsonResponse({"msg":"this is your Jimmisoft app"})
    except Exception as error:
        return JsonResponse({"error":str(error)}, status=500)
    

api_view(['POST'])
permission_classes([])
@csrf_exempt
def fetch_adhar_card_data_views(request):
    try:
        # Generate a random UUID
        generated_uuid = uuid.uuid4()

        # Convert the UUID to a string
        uuid_string = str(generated_uuid)[:10]

        # print("Generated UUID:", uuid_string)
        prd_setting = cuf.get_prd_setting()
        upload_files = request.FILES['files']
        password = request.POST['password']
        local_path = save_file_based_on_extension(prd_setting, upload_files)
        decripted_path = remove_pdf_password(local_path, password)
        res_metadata = extract_text_with_coordinates(decripted_path)
        output_path = f'media/adhar_{uuid_string}'
        # print("output_path", uuid_string)
        final_data = get_all_page_text(res_metadata)
        adhar_json = get_adhar_json_data(final_data)
        # adno = adhar_json['aadharNo']
        # if adno:
        res_output_path = extract_image.extract_image_from_pdf(decripted_path, output_path)
        pics_path = res_output_path+'/image_1_5.png'
        qrcode_path = res_output_path+'/image_1_12.png'
        # output_image_path = f'media/image_{uuid_string}'
        pics_base64 = base64.image_to_base64(pics_path)
        qrcode_base64 = base64.image_to_base64(qrcode_path)
        adhar_json["pics_base64"] = pics_base64
        adhar_json["qrcode_base64"] = qrcode_base64
        line_no = find_line_no.extract_text_from_region(decripted_path)
        x= 309.2
        y= 600
        w= 150
        h= 6*(line_no-1)
        hindi_address_output_path =  f'media/adhar_{uuid_string}/hindi_address.png'
        hindi_name_output_path =  f'media/adhar_{uuid_string}/hindi_name.png'
        hindi_address_path = screenshot.capture_screenshot(decripted_path, hindi_address_output_path, x, y, w, h, 1600)
        x = 115  # Replace with your X-axis position
        y = 600  # Replace with your Y-axis position
        w = 145  # Replace with the width you desire
        h = 40  # Replace with the height you desire
        hindi_name_path = screenshot.capture_screenshot(decripted_path, hindi_name_output_path, x, y, w, h, 1600)
        # print ("hindi_address_path", hindi_address_path)
        # print ("hindi_name_path", hindi_name_path)
        hindi_add_path_wws = remove_background_whitespace.remove_background_and_whitespace(hindi_address_path, hindi_address_path)
        hindi_name_path_wws=remove_background_whitespace.remove_background_and_whitespace(hindi_name_path, hindi_name_path)
        hindi_add_path_wws_base64 = base64.image_to_base64(hindi_add_path_wws)
        hindi_name_path_wws_base64 = base64.image_to_base64(hindi_name_path_wws)
        adhar_json["hindi_address_base64"] = hindi_add_path_wws_base64
        adhar_json["hindi_name_base64"] = hindi_name_path_wws_base64
       


        # print("line_no",line_no)
        # print("localpath", local_path, password)
        # print("res_path", decripted_path)
        # print("res_output_path", res_output_path)
        return JsonResponse({"msg":adhar_json}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return JsonResponse({"error":str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

import pikepdf

def remove_pdf_password(pdf_path, password):
    """Removes password from a PDF file."""
    try:
        with pikepdf.open(pdf_path, password=password) as pdf:
            pdf.save(pdf_path.replace(".pdf", "_decrypted.pdf"))
        return pdf_path.replace(".pdf", "_decrypted.pdf")
        # print(f"Password removed successfully! Decrypted file saved as: {pdf_path.replace('.pdf', '_decrypted.pdf')}")
    except pikepdf._qpdf.PasswordError:
        print("Incorrect password provided. Please try again.")

def get_all_page_text(docs_metadata_json):
    """
        function help us to get only content from metadata
    
    """
    all_page_text = []

    # Iterate over each page in the message
    for page, items in docs_metadata_json.items():
        # Initialize an empty string to store the text from the current page
        page_text = ""

        # Iterate over each item on the page
        for item in items:
            # Concatenate the text with a space separator
            page_text += item["text"] + " "

        # Append the page text to the all_page_text array
        all_page_text.append(page_text.strip())  # Remove leading/trailing whitespaces
        
        # print("all_page_text",all_page_text)
        return all_page_text[0]
    

def get_adhar_json_data(data):
    # Extract mobile number
    mobile_index = data.find("Mobile:") + 7
    mobile_number = data[mobile_index:mobile_index + 11]

    # Extract VID number
    vid_index = data.rfind("VID :") + 6
    vid_number = data[vid_index:vid_index + 19]

    # Extract address
    address_index = data.find("Address:") + 9
    address = data[address_index:vid_index - 1].replace(vid_number, "")

    # Create final dictionary
    final_obj = {
        "aadharNo": vid_number[:15],  # Extract Aadhaar number from VID
        "address": address,
        "vidNo": vid_number,
        "mobNo": mobile_number,
    }
    return final_obj

api_view(['POST'])
permission_classes([])
@csrf_exempt
def fetch_pan_card_data_views(request):
    try:
        generated_uuid = uuid.uuid4()

        # Convert the UUID to a string
        uuid_string = str(generated_uuid)[:10]

        # print("Generated UUID:", uuid_string)
        prd_setting = cuf.get_prd_setting()
        upload_files = request.FILES['files']
        password = request.POST['password']
        local_path = save_file_based_on_extension(prd_setting, upload_files)
        decripted_path = remove_pdf_password(local_path, password)
        res_metadata = extract_text_with_coordinates(decripted_path)
        output_path = f'media/pan_{uuid_string}'
        # print("output_path", uuid_string)
        final_data = get_all_page_text(res_metadata)
        # pan_json = get_pan_json_data(final_data)
        # print ("final_data", final_data)
        pan_json = makeJson.make_pan_card_json(final_data)
        # print(res_json)
        res_output_path = extract_image.extract_image_from_pdf(decripted_path, output_path)
        pics_path = res_output_path+'/image_1_3.png'
        qrcode_path = res_output_path+'/image_1_2.png'
        # output_image_path = f'media/image_{uuid_string}'
        pics_base64 = base64.image_to_base64(pics_path)
        qrcode_base64 = base64.image_to_base64(qrcode_path)
        pan_json["pics_base64"] = pics_base64
        pan_json["qrcode_base64"] = qrcode_base64



        print("line_no")
        # print("localpath", local_path, password)
        # print("res_path", decripted_path)
        # print("res_output_path", res_output_path)
        return JsonResponse({"msg":pan_json}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return JsonResponse({"error":str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
