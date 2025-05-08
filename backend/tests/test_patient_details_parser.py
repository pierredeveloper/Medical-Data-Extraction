import sys
import os
import pytest

# Ensure the correct import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from parser_patient_details import PatientDetailsParser  # Now resolves correctly

@pytest.fixture
def doc_1_kathy():
    document_kathy = '''
    17/12/2020
    
     
    
    Patient Medical Record
    
     
    
     
    
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 '
    United States Height:
    190
    In Casc of Emergency
    7 7
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    
    Genera! Medical History
    
    a
    
    ee
    
    nh ee A OE i ne
    
    Chicken Pox (Varicella): Measies:
    
    IMMUNE IMMUNE
    
    Have you had the Hepatitis B vaccination?
    No
    
    List any Medical Problems (asthma, seizures, headaches):
    
    Migraine
        '''
    return PatientDetailsParser(document_kathy)

@pytest.fixture
def doc_2_jerry():
    document_jerry = '''
    17/12/2020
    
    Patient Medical Record
    
    Patient Information Birth Date
    
    Jerry Lucas May 2 1998
    
    (279) 920-8204 Weight:
    
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201 Height:
    
    United States gnt
    170
    
    In Case of Emergency |
    meee
    
    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    
    Home phone United States "
    Work phone
    
    General Medical History
    
     
    
    Chicken Pox (Varicelia): Measles: ..
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    Yes
    
    List any Medical Problems (asthma, seizures, headaches):
    N/A
        '''
    return PatientDetailsParser(document_jerry)

@pytest.fixture()
def doc_empty():
    return PatientDetailsParser("")

def test_get_name(doc_1_kathy, doc_2_jerry, doc_empty):
    assert doc_1_kathy.get_field('patient_name') == 'Kathy Crawford'
    assert doc_2_jerry.get_field('patient_name') == 'Jerry Lucas'
    assert doc_empty.get_field('patient_name') == None

def test_get_phone_number(doc_1_kathy, doc_2_jerry, doc_empty):
    assert doc_1_kathy.get_field('phone_number') == '(737) 988-0851'
    assert doc_2_jerry.get_field('phone_number') == '(279) 920-8204'
    assert doc_empty.get_field('phone_number') == None

def test_get_hepatitis_b_vaccination(doc_1_kathy, doc_2_jerry, doc_empty):
    assert doc_1_kathy.get_field('hepatitis_b_vaccination') == 'No'
    assert doc_2_jerry.get_field('hepatitis_b_vaccination') == 'Yes'
    assert doc_empty.get_field('hepatitis_b_vaccination') == None

def test_get_medical_problem(doc_1_kathy, doc_2_jerry, doc_empty):
    assert doc_1_kathy.get_field('medical_problem') == 'Migraine'
    assert doc_2_jerry.get_field('medical_problem') == 'N/A'
    assert doc_empty.get_field('medical_problem') == None

def test_parse(doc_1_kathy, doc_2_jerry, doc_empty):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['phone_number'] == '(737) 988-0851'
    assert record_kathy['hepatitis_b_vaccination'] == 'No'
    assert record_kathy['medical_problem'] == 'Migraine'

    record_jerry = doc_2_jerry.parse()
    assert record_jerry['patient_name'] == 'Jerry Lucas'
    assert record_jerry['phone_number'] == '(279) 920-8204'
    assert record_jerry['hepatitis_b_vaccination'] == 'Yes'
    assert record_jerry['medical_problem'] == 'N/A'

    record_empty = doc_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'phone_number': None,
        'hepatitis_b_vaccination': None,
        'medical_problem': None
    }


