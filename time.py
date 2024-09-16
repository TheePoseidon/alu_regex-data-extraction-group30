import re
time_24h_pattern = r"\d{2}:\d{2}"
time_12h_pattern = r"\d{1,2}:\d{2} (AM|PM)"

def extract_time(text):
    matches_24h = re.findall(time_24h_pattern, text)
    matches_12h = re.findall(time_12h_pattern, text)
    return matches_24h + matches_12h
