import re

List = ['784516497949848484674949', '8477802902','9639334242']

for i in List:
	result = re.findall(r'[7-9]{1}[0-9]{9}', i)
	if result:
		print(result, end =" ")