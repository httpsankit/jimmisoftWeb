import re

def make_pan_card_json(data):
    pan_regex = re.compile(r'Cut ([A-Z]{5}\d{4}[A-Z])')
    dob_regex = re.compile(r'(\d{2}/\d{2}/\d{4})')
    gender_regex = re.compile(r'(Male|Female)')

    pan_match = pan_regex.search(data)
    dob_match = dob_regex.search(data)
    gender_match = gender_regex.search(data)

    if pan_match and dob_match:
        pan_card_no = pan_match.group(1)
        dob = dob_match.group(1)
        gender = gender_match.group(1)

        # Find indices of PAN Card number and "Application"
        pan_index = data.find(gender)
        application_index = data.find("PAN Application")

        # Extract the name between PAN Card number and "Application"
        name = data[pan_index:application_index].replace(gender, "").strip()
        name_index = data.rfind(name)
        digital_sign_index = data.find("Digitally signed by")
        father_name = data[name_index:digital_sign_index].replace(name, "").strip()

        return {
            'panCardNo': pan_card_no,
            'dob': dob,
            'gender': gender,
            'name': name,
            'fatherName': father_name
        }
    else:
        return None  # Return None if any required information is not found in the data
    



    
