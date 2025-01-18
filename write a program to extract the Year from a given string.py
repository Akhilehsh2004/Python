import re

result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'My name is Akhilesh Pant, My joining Date is 11-01-2025')

print("Year Of Appointment Is:", result)