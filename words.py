
count = 0
def process_word(word):
	word = word.strip()
	if len(word) > 20:
		global count
		count = count + 1
		print(word)



def has_no_e(word):
	if 'e' not in word:
		print(word)
		global count
		count = count + 1

fin = open('words.txt')

for word in fin:
	#has_no_e(word)
	process_word(word)
print(count)
