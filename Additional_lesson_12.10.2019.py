'''input_string = input("Enter some string : ")

for i in range(len(input_string)):
	input_string[i] = input_string[i].upper()
print(input_string)


input_string = input("Enter some string : ")
new_list = []

for i in range(len(input_string)):
	new_list.append(input_string[i].upper())

input_string = ""
print(new_list)
print(input_string.join(new_list))

def calculate_members(string):
	digits = 0
	letters = 0
	for char in string:
		if char.isalpha():
			letters += 1
		if char.isdigit():
			digits += 1
	return digits , letters


user_string = input("Enter some string: ")
digits, letters = calculate_members(user_string)
print("Num of digits ", digits, "and number of letters ", letters)'''


import random
import string

def randomString(stringlenght=1):
	letters = string.ascii_lowercase
	return "".join(random.choice(letters) for i in range(stringlenght))


	


def guess_letters():
	guess = False
	while not guess:
		letter = input("Enter a letter ")
		while not letter.isalpha() and len(letter) == 1:
			print("You have entered wrong character ")
			letter = input("Enter a letter ")
		
	return guess, letter

a = randomString()
if a == letter:
	count += 1
	print(count)
randomString()

print(guess_letters())