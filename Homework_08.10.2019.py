# replace letter program
text = input("Enter text:\n")
changed_text = text[1:len(text)].replace(text[0], "$")
print(text[0]+changed_text)

# ing to ly changing program
def string_changer(text2):
	count = 0
	for i in text2:
		count +=1
	
	if count == 3 and text2[-3:len(text2)] != "ing":
		text2 = text2 + "ing"
		print(text2)
	elif count != 3 and text2[-3:len(text2)] == "ing":
		text2 = text2 + "ly"
		print(text2)
	elif count < 3:
		print("The input character's number is not enough!")
	elif count > 3:
		print("The input character's number is more than need!")

text2 = input("Enter text:\n")
string_changer(text2)

# The meaning raplacing program
text3 = input("Enter the sentence:\n")
if text3.find("poor", 0, len(text3)) - text3.find("not", 0, len(text3)) > 0 and text3.find("not", 0, len(text3)) != -1:
	text3 = text3[0:len(text3)].replace("poor","good")
	text3 = text3[0:len(text3)].replace("not ","")
	print(text3)
else:
	print("The result is:\n",text3)