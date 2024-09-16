import re

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9./-]+\.[a-zA-Z]{2,6}(?:/[a-zA-Z0-9_./#+-]*)?'
    return re.findall(pattern, text)
