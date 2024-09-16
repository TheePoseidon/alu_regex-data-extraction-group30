import re

currency_pattern = r"[$€£]\d+(?:\.\d+)?(?:,\d{3})*"

def extract_currencies(text):
    matches = re.findall(currency_pattern, text)
    return matches
