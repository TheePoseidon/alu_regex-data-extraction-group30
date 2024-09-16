import re

def extract_hashtags(text):
    pattern = r'\B#\w+[a-zA-Z]+\b'
    return re.findall(pattern, text)
