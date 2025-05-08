# import pdf2image to convert pdf to image
from pdf2image import convert_from_path
import pytesseract
import utility
import sys
import os
# Ensure the correct import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser


POPPER_PATH = "/home/pierre/miniconda3/bin"
# Specify where google tesseract OCR is installed in the computer
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract(file_path, file_data):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPER_PATH)
    document_text = ''

    if len(pages) > 0:
        page = pages[0]
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    #return document_text

    # Extract fields from text
    if file_data == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()  # extract data for prescription
    elif file_data == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()   # extract data for patient details
    else:
        raise Exception(f"Invalid document fromat: {file_data}")

    return extracted_data

if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)
