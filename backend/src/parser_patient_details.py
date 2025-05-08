from parser_generic import PatientDocParser
import re

class PatientDetailsParser(PatientDocParser):
    def __init__(self, text):
        PatientDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'hepatitis_b_vaccination': self.get_field('hepatitis_b_vaccination'),
            'medical_problem': self.get_field('medical_problem')
        }

    def get_field(self, field_name):
            pattern_dic = {
                'patient_name': {
                    'pattern': r"([A-Z][a-z]+ [A-Z][a-z]+)\s+[A-Z][a-z]+ \d{1,2} \d{4}",
                    'flags': 0
                },
                'phone_number': {
                    'pattern': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
                    'flags': 0
                },
                'hepatitis_b_vaccination': {
                    'pattern': 'Have you had the Hepatitis B vaccination\?.*(Yes|No)',
                    'flags': re.DOTALL
                },
                'medical_problem': {
                    'pattern': r"List any Medical Problems.*?:\s*([^\n]+)",
                    'flags': re.DOTALL
                }
            }

            pattern_object = pattern_dic.get(field_name)
            if pattern_object:
                matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
                if matches:
                    return matches[0].strip()
            return None


if __name__ == '__main__':
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

    pp = PatientDetailsParser(document_kathy)
    print(pp.parse())


