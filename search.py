
def find(word, letter, start=0):
	index = start 
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1


if __name__ == '__main__':
	print(find("Harikesav", 'k'))
	print(find("Harikesav", 'k', 5))
