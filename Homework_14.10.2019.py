import random
import string

def randomString(stringlenght=3):
	letters = string.ascii_lowercase
	return "".join(random.choice(letters) for i in range(stringlenght))

a = randomString()
print(a)
g = a

def guess_program(string,string_2=""):
	
	for i in string:
		
		for j in string_2:
			if i == j:
				string = string.replace(j, '')
				
	return  string

c = guess_program(g)

while c != "":
	b = input(" Enter an any letter: ")
	while not (b.isalpha() and len(b)==1):
                print("you have entered wrong character")
                b=input(" Enter an any letter: ")

	c = guess_program(g,b)
	#print(c)
	g = c
	
else:
	#print(a)
	print(" You found the word! ",a)
