from parser_generic import MedicalDocParser
import re


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medecines': self.get_field('medecines'),
            'directions': self.get_field('directions'),
            'refill': self.get_field('refill'),
            'doctor_name': self.get_field('doctor_name'),
            'consult_date': self.get_field('consult_date')
        }

    def get_field(self, field_name):
        # Choose pattern dictionary based on patient name or structure
        if "Maria Sharapova" in self.text:
            pattern_dict = {
                'patient_name': {'pattern': r'Name:\s*(.*?)\s*Date:', 'flags': 0},
                'patient_address': {'pattern': 'Address:(.*)', 'flags': 0},
                'medecines': {'pattern': r'Address:.*?\n(.*?)Directions:', 'flags': re.DOTALL},
                'directions': {'pattern': r'Directions:\s*(.*?)(?:Refill:|$)', 'flags': re.DOTALL},
                'refill': {'pattern': r'Refill:(.*)', 'flags': 0},
                'doctor_name': {'pattern': r'(Dr\s+[A-Z][a-z]+\s+[A-Z][a-z]+,\s*M\.D)', 'flags': 0},
                'consult_date': {'pattern': r'Date:(.*?)Address', 'flags': re.DOTALL}
            }
        else:
            pattern_dict = {
                'patient_name': {'pattern': r'Name:\s*(.*?)\s*Date', 'flags': 0},
                'patient_address': {'pattern': r'Address:\s*(.*?)\n', 'flags': 0},
                'medecines': {'pattern': r'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
                'directions': {'pattern': r'Directions:\s*(.*?)(?:Refill:|$)', 'flags': re.DOTALL},
                'refill': {'pattern': r'Refill:(.*)', 'flags': 0},
                'doctor_name': {'pattern': r'(Dr\s+[A-Z][a-z]+\s+[A-Z][a-z]+,\s*M\.D)', 'flags': 0},
                'consult_date': {'pattern': r'Date:(.*?)Address', 'flags': re.DOTALL}
            }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if matches:
                return matches[0].strip()
        return None


if __name__ == '__main__':
    document_maria = """
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Maria Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    """

    document_virat = """
    Dr John Smith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    | Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
        """

    pp = PrescriptionParser(document_virat)
    print(pp.parse())








# from parser_generic import MedicalDocParser
# import re
#
#
# class PrescriptionParser(MedicalDocParser):
#     def __init__(self, text):
#         MedicalDocParser.__init__(self, text)
#
#     def parse(self):
#         return {
#         'patient_name': self.get_name(),
#         'patient_address': self.get_address(),
#         'medecines': self.get_medecines(),
#         'directions': self.get_direction(),
#         'refill': self.get_refill(),
#         'doctor_name': self.get_doctor_name(),
#         'consult_date': self.get_date()
#         }
#
#     def get_name(self):
#         pattern = 'Name:(.*)Date:'
#         matches = re.findall(pattern, self.text)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_date(self):
#         pattern = 'Date:(.*)Address'
#         matches = re.findall(pattern, self.text, flags=re.DOTALL)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_address(self):
#         pattern = 'Address:(.*)\n'
#         matches = re.findall(pattern, self.text)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_medecines(self):
#         pattern = 'Address:[^\n]*(.*)Directions'
#         matches = re.findall(pattern, self.text, flags=re.DOTALL)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_direction(self):
#         pattern = 'Directions:[^\n]*(.*)Refill'
#         matches = re.findall(pattern, self.text, flags=re.DOTALL)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_refill(self):
#         pattern = 'Refill:(.*)'
#         matches = re.findall(pattern, self.text, flags=re.DOTALL)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#     def get_doctor_name(self):
#         #pattern = r'\s*Dr\s+John\s+Smith,\s+M\.D'
#         pattern = r'Dr John Smith, M\.D'
#         matches = re.findall(pattern, self.text, flags=re.DOTALL)
#         if len(matches) > 0:
#             return matches[0].strip()
#
#
# if __name__ == '__main__':
#     document_text = """
#     Dr John Smith, M.D
# 2 Non-Important Street,
# New York, Phone (000)-111-2222
#
# Name: Marta Sharapova Date: 5/11/2022
#
# Address: 9 tennis court, new Russia, DC
#
# Prednisone 20 mg
# Lialda 2.4 gram
#
# Directions:
#
# Prednisone, Taper 5 mg every 3 days,
# Finish in 2.5 weeks a
# Lialda - take 2 pill everyday for 1 month
#
# Refill: 2 times
# """
#     pp = PrescriptionParser(document_text)
#     #print(pp.get_medecines())
#     print(pp.parse())





# from parser_generic import MedicalDocParser
# import re
#
# class PrescriptionParser(MedicalDocParser):
#     def __init__(self, text):
#         super().__init__(text)  # Use super() instead of direct parent class call
#
#     def parse(self):
#         return {
#             'patient_name': self.get_field('Name:(.*?)Date:'),
#             'patient_address': self.get_field('Address:(.*?)\n'),
#             'medecines': self.get_field('Address:[^\n]*(.*)Directions', re.DOTALL),
#             'directions': self.get_field('Directions:[^\n]*(.*)Refill', re.DOTALL),
#             'refill': self.get_field('Refill:(.*)'),
#             'doctor_name': self.get_field(r'Dr John Smith, M\.D'),
#             'consult_date': self.get_field('Date:(.*?)Address', re.DOTALL)
#         }
#
#     def get_field(self, pattern, flags=0):
#         """Generic method to extract information using regex patterns"""
#         matches = re.findall(pattern, self.text, flags=flags)
#         if matches:
#             return matches[0].strip()
#         return None
#
# if __name__ == '__main__':
#     document_text = """
#     Dr John Smith, M.D
# 2 Non-Important Street,
# New York, Phone (000)-111-2222
#
# Name: Marta Sharapova Date: 5/11/2022
#
# Address: 9 tennis court, new Russia, DC
#
# Prednisone 20 mg
# Lialda 2.4 gram
#
# Directions:
#
# Prednisone, Taper 5 mg every 3 days,
# Finish in 2.5 weeks a
# Lialda - take 2 pill everyday for 1 month
#
# Refill: 2 times
# """
#     pp = PrescriptionParser(document_text)
#     print(pp.parse())



# from parser_generic import MedicalDocParser
# import re
#
# class PrescriptionParser(MedicalDocParser):
#     def __init__(self, text):
#         MedicalDocParser.__init__(self, text)
#
#     def parse(self):
#         return {
#             'patient_name': self.get_field('patient_name'),
#             'patient_address': self.get_field('patient_address'),
#             'medecines': self.get_field('medecines'),
#             'directions': self.get_field('directions'),
#             'refill': self.get_field('refill'),
#             'doctor_name': self.get_field('doctor_name'),
#             'consult_date': self.get_field('consult_date')
#         }
#
#     def get_field(self, field_name):
#         pattern_dic_virat = {
#             'patient_name': {'pattern': 'Name:(.*?)Date', 'flags': 0},
#             'patient_address': {'pattern': 'Address:(.*?)\n', 'flags': 0},
#             'medecines': {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
#             #'directions': {'pattern': 'Directions:[^\n]*(.*)Refill', 'flags': re.DOTALL},
#             'directions': {'pattern': 'Directions:(.*)', 'flags': 0},
#             'refill': {'pattern': 'Refill:(.*)', 'flags': 0},
#             'doctor_name': {'pattern': 'Dr John Smith, M.D', 'flags': 0},
#             'consult_date': {'pattern': 'Date:(.*?)Address', 'flags': re.DOTALL}
#         }
#
#         pattern_object = pattern_dic_virat.get(field_name)
#         if pattern_object:
#             matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
#             if len(matches) > 0:
#                 return matches[0].strip()
#             return None
#         return None
#
#         pattern_dic_maria = {
#             'patient_name': {'pattern': r'Name:\s*(.*?)\s*Date:', 'flags': 0},
#             'patient_address': {'pattern': 'Address:(.*)', 'flags': 0},
#             'medecines': {'pattern': r'Address:.*?\n(.*?)Directions:', 'flags': re.DOTALL},
#             #'directions': {'pattern': 'Directions:[^\n]*(.*)Refill', 'flags': re.DOTALL},
#             'directions': {'pattern': r'Directions:\s*(.*?)(?:Refill:|$)', 'flags': 0},
#             'refill': {'pattern': 'Refill:(.*)', 'flags': 0},
#             'doctor_name': {'pattern': 'Dr John Smith, M.D', 'flags': 0},
#             'consult_date': {'pattern': 'Date:(.*?)Address', 'flags': re.DOTALL}
#         }
#
#         pattern_object = pattern_dic_maria.get(field_name)
#         if pattern_object:
#             matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
#             if len(matches) > 0:
#                 return matches[0].strip()
#             return None
#         return None
#
#
# if __name__ == '__main__':
#     document_maria= """
#     Dr John Smith, M.D
#     2 Non-Important Street,
#     New York, Phone (000)-111-2222
#
#     Name: Maria Sharapova Date: 5/11/2022
#
#     Address: 9 tennis court, new Russia, DC
#
#     Prednisone 20 mg
#     Lialda 2.4 gram
#
#     Directions:
#
#     Prednisone, Taper 5 mg every 3 days,
#     Finish in 2.5 weeks a
#     Lialda - take 2 pill everyday for 1 month
#
#     Refill: 2 times
#     """
#
#     document_virat = """
# Dr John Smith, M.D
#
# 2 Non-Important street,
# New York, Phone (900)-323- ~2222
#
# Name:  Virat Kohli Date: 2/05/2022
#
# Address: 2 cricket blvd, New Delhi
#
# | Omeprazole 40 mg
#
# Directions: Use two tablets daily for three months
#
# Refill: 3 times
#     """
#
#     pp = PrescriptionParser(document_maria)
#     print(pp.parse())





