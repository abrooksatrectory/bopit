print("hi")
print("woo")

f = open("sample3.txt", "r")
s = f.read()
#s = "woooooooooo, good, bad, yes, bo, no, yo, yep. Noooooooooooooooooooooo."
# Splits the string into words, using the spaces in the string.
words = s.split()
# Initialize some empty variables
complete = []
add = 0

print(words)

# Sum the word's lengths and remove punctuation
for word in words:
	# Checks words for punctuation
	if "," in word or "." in word:
		# Removing the last character
		word = word[:-1]
	complete.append(word)
	add = add +len(word)

# Finding average length
mean = add/len(words)
	
print(complete)
print(mean)

