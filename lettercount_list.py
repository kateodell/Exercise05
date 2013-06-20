import string
from sys import argv
# input file and get string of the contents
script, file_name = argv

file_content = open(file_name)
file_text = file_content.read()
file_content.close()

# initialize alphabet dictionary, with keys a-z value = 0
alpha_count = [0] * 26

# iterate through each character in the file content string
for char in file_text:
	if char in string.ascii_letters:
		alpha_count[ord(char.lower())-ord('a')] += 1

# print "We've counted the rate of appearance of each letter in the text: "

for num in alpha_count:
	print num

#print alpha_count
