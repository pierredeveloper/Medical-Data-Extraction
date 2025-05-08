from parser_generic import InsuranceDocParser
import re

class InsuranceDetailsParser(InsuranceDocParser):
    def __init__(self, text):
        InsuranceDocParser.__init__(self, text)

    def parse(self):
        return {
            'insurance_name': self.get_field('insurance_name'),
            'address': self.get_field('address'),
            'policy_number': self.get_field('policy_number'),
            'expiry_date': self.get_field('expiry_date'),
            'medical_history': self.get_field('medical_history'),
        }

    def get_field(self, field_name):
            pattern_dic = {
                'insurance_name': {
                    'pattern': r"Name of Insurance Company:\s*(.*?)\s*(?:Address:|\n[A-Z]|$)",
                    'flags': re.DOTALL
                },
                'address': {
                    'pattern': "Address:[^\n]*(.*)Policy Number",
                    'flags': re.DOTALL
                },
                'policy_number': {
                    'pattern': "Policy Number:[^\n]*(.*)Expiry Date",
                    'flags': re.DOTALL
                },
                'expiry_date': {
                    'pattern': r"\b\d{1,2} [A-Za-z]+ \d{4}\b",
                    'flags': re.DOTALL
                },
                'medical_history': {
                    'pattern': "Medical Insurance Details:(.*)\n",
                    'flags': re.DOTALL
                },
            }

            pattern_object = pattern_dic.get(field_name)
            if pattern_object:
                matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
                if matches:
                    return matches[0].strip()
            return None


if __name__ == '__main__':
    document_text_2 = '''

    Name of Insurance Company:
    Random Insuarance Company 

    Address: 
    4789 Bollinger Rd, Jersey City, New Jersey, 07030

    Policy Number:
    7115207313 

    Expiry Date: 30 December 2020

    Do you have medical insurance?
    Yes

    Medical Insurance Details:
    List any allergies: Peanuts, 'List any medication taken regularly': Triptans

    '''

    pp = InsuranceDetailsParser(document_text_2)
    print(pp.parse())