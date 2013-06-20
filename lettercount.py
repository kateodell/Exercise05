import string
from sys import argv
# input file and get string of the contents
script, file_name = argv

file_content = open(file_name)
file_text = file_content.read()
file_content.close()

# initialize alphabet dictionary, with keys a-z value = 0
alpha_count = {}
for char in string.ascii_lowercase:
	alpha_count[char] = 0

# iterate through each character in the file content string
for char in file_text:
	if char in string.ascii_letters:
		alpha_count[char.lower()] += 1

print "We've counted the rate of appearance of each letter in the text: "
print alpha_count
# check if it is a letter. if so, convert to lower and increment count(value) for that letter