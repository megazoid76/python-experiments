import re

str = 'an example word:e'
match = re.search(r'word:.', str)
# If-statement after search() tests if it succeeded
if match:                      
	print 'found', match.group() ## 'found word:cat'
else:
	print 'did not find'
