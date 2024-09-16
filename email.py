import re

email_pattern = r"[\w\.\+\-]+@[a-zA-Z\d\-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?"

def extract_emails(text):
    matches = re.findall(email_pattern, text)
    return matches
