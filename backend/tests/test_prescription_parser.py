import sys
import os
import pytest

# Ensure the correct import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from parser_prescription import PrescriptionParser  # Now resolves correctly

@pytest.fixture
def doc_1_marta():
    document_text = """
        Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    """
    return PrescriptionParser(document_text)

@pytest.fixture
def doc_2_pierre():
    document_text = """
        Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Pierre Jean Bien-Aime Date: 5/13/2022

    Address: Cale Trine de Moya #7, La Romana, DR

    Amoxicillin 500 mg
    Ibuprofen 200 mg

    Directions:

    Amoxicillin - take 1 capsule three times daily for 7 days
    Ibuprofen - take 1 tablet every 6 hours as needed for pain

    Refill: 3 times
    """
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser("")

def test_get_name(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_pierre.get_field('patient_name') == 'Pierre Jean Bien-Aime'
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('patient_address') == "9 tennis court, new Russia, DC"
    assert doc_2_pierre.get_field('patient_address') == "Cale Trine de Moya #7, La Romana, DR"
    assert doc_3_empty.get_field('patient_address') == None

def test_get_refill(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('refill') == "2 times"
    assert doc_2_pierre.get_field('refill') == "3 times"
    assert doc_3_empty.get_field('refill') == None

def test_get_medecines(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('medecines') == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert doc_2_pierre.get_field('medecines') == 'Amoxicillin 500 mg\n    Ibuprofen 200 mg'
    assert doc_3_empty.get_field('medecines') == None

def test_get_directions(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take 2 pill everyday for 1 month'
    assert doc_2_pierre.get_field('directions') == 'Amoxicillin - take 1 capsule three times daily for 7 days\n    Ibuprofen - take 1 tablet every 6 hours as needed for pain'
    assert doc_3_empty.get_field('directions') == None

def test_get_doctor_name(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('doctor_name') == 'Dr John Smith, M.D'
    assert doc_2_pierre.get_field('doctor_name') == 'Dr John Smith, M.D'
    assert doc_3_empty.get_field('doctor_name') == None

def test_get_consult_date(doc_1_marta, doc_2_pierre, doc_3_empty):
    assert doc_1_marta.get_field('consult_date') == '5/11/2022'
    assert doc_2_pierre.get_field('consult_date') == '5/13/2022'
    assert doc_3_empty.get_field('consult_date') == None


def test_parse(doc_1_marta, doc_2_pierre, doc_3_empty):
    record_marta = doc_1_marta.parse()
    assert record_marta['patient_name'] == 'Marta Sharapova'
    assert record_marta['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_marta['medecines'] == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert record_marta['directions'] == 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take 2 pill everyday for 1 month'
    assert record_marta['refill'] == '2 times'
    assert record_marta['doctor_name'] == 'Dr John Smith, M.D'
    assert record_marta['consult_date'] == '5/11/2022'

    record_pierre = doc_2_pierre.parse()
    assert record_pierre['patient_name'] == 'Pierre Jean Bien-Aime'
    assert record_pierre['patient_address'] == 'Cale Trine de Moya #7, La Romana, DR'
    assert record_pierre['medecines'] == 'Amoxicillin 500 mg\n    Ibuprofen 200 mg'
    assert record_pierre['directions'] == 'Amoxicillin - take 1 capsule three times daily for 7 days\n    Ibuprofen - take 1 tablet every 6 hours as needed for pain'
    assert record_pierre['refill'] == '3 times'
    assert record_pierre['doctor_name'] == 'Dr John Smith, M.D'
    assert record_pierre['consult_date'] == '5/13/2022'

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medecines': None,
        'directions': None,
        'refill': None,
        'doctor_name': None,
        'consult_date': None
    }


