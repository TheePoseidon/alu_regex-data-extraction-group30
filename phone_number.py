import re
 phone_number_pattern = r"\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}"
 def extract_phone_numbers(text):
 matches = re.findall(phone_number_pattern, text)
 return matches
