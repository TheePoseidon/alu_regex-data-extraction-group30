#!/usr/bin/env python

# Importing the functions
from email import extract_emails
from URLs import extract_urls
from phone_number import extract_phone_numbers
from credit_cards import extract_credit_cards
from times import extract_time
from HTML_tags import extract_html_tags
from hashtags import extract_hashtags
from currency import extract_currencies

# Sample text
text = """
My email is john.doe@example.com and my website is https://www.example.com.
You can contact me at 123-456-7890 or (123) 456-7890. 
My credit card number is 1234 5678 9123 4567, and I made a purchase at 14:30.
Check out <div class="container"> and <img src="logo.png"/> on my site. 
Don't forget #python and I spent $99.99.
"""

# Extracting data
emails = extract_emails(text)
URLs = extract_urls(text)
phone_numbers = extract_phone_numbers(text)
credit_cards = extract_credit_cards(text)
times = extract_time(text)
html_tags = extract_html_tags(text)
hashtags = extract_hashtags(text)
currencies = extract_currencies(text)

# Printing the results
print("Emails:", emails)
print("URLs:", URLs)
print("Phone Numbers:", phone_numbers)
print("Credit Cards:", credit_cards)
print("Times:", times)
print("HTML Tags:", html_tags)
print("Hashtags:", hashtags)
print("Currencies:", currencies)
