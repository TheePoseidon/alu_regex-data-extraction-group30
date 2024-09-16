#!/usr/bin/env python3
import re

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)
