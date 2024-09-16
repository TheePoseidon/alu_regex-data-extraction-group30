import re

def extract_html_tags(text):
    pattern = r'<\/?\w+[^>]*>'
    return re.findall(pattern, text)
