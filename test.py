import re


names = dir(re)

result = []
for name in dir(re):
	#match = re.search('find', name)
	if 'find' in name:
		result.append(name)

print(result)
