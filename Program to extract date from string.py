import re

pattern = r'\d{2}-\d{2}-\d{4}'

string = "The event is scheduled for 11-01-2025. Please mark your calendar."

match = re.search(pattern, string)

if match:
    print("Date found:", match.group())
else:
    print("No Match")