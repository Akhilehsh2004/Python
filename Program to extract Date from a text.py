import re

# Regular expression pattern for a date in the format DD/MM/YYYY, DD-MM-YYYY, or YYYY-MM-DD
pattern = r"\b\d{1,4}[-/]\d{1,2}[-/]\d{1,4}\b"

string = "The event is scheduled for 11-01-2025. Please mark your calendar."

match = re.search(pattern, string)

if match:
    print("Date found:", match.group())
else:
    print("No Match")