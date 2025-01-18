import re 

pattern = r"[\w.-]+@[\w.-]+"

string = "Please send your feedback at akhileshpant2004@gmail.com, And if any doubt sp mail me at  akhileshpant@outlook.com. Mail at daredevil613@gmail.com for the rest"

match = re.findall(pattern, string)

if match:
	print("Email Found")
	for email in match:
		print(email)
else:
	print("No Match")
