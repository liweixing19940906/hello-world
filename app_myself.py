# Pay attention:indentation is Tab
import json
from difflib import get_close_matches 

file = open("data.json", 'r')
data = json.load(file)

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		print("Did you mean %s ? Please continue" % word.title())
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did You mean %s ? enter Y for yes,enter N for No:  " % get_close_matches(word, data.keys())[0])
		if (yn == "Y") or (yn == "y"):
			return data[get_close_matches(word, data.keys())[0]]
		elif (yn == "N") or (yn == "n"):
			return "The word you enter doesn't exist, please check your input"
		else:
			return "invalid input, Please input 'y' or 'n' "
	else:
		return "The word doesn't exist. Please check it"

while(True):
	word = input("Enter word: ")
	output = translate(word)
	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)

