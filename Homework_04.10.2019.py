# Kilometers to miles convert program with a little bit difference program runing steps
def kilotomiles(number):
	number = number*0.62
	return number
number = int(input("Input kilometers: "))
print((kilotomiles(number)), "miles")

def kilotomiles(number):
	number = number*0.62
	print(number, "miles")
number = int(input("Input kilometers: "))
kilotomiles(number)

#Celsius to fahrenheit convert program
def celtofar(temp):
	temp = temp*1.8+32
	return temp
temp = int(input("Input temperature in celsius: "))
print((celtofar(temp)), "fahrenheit")

def celtofar(temp):
	temp = temp*1.8+32
	print(temp, "fahrenheit")
temp = int(input("Input temperature in celsius: "))
(celtofar(temp))

#word counter in sentence
def wordcounter(sent):
	count = 0
	j = sent[0]
	for i in sent[1:len(sent)]:
		if i != " " and j == " ":
			#print(i, "start")
			pass
		if i == " " and j != " ":
			#print(i, "end")
			count += 1
		j = i

	if sent.endswith(" ") == False:
		return count + 1
	else:
		return count

sent = input("write a sentence: ")
print(wordcounter(sent))


#symbol checker program
def symbol_checker(sent):
	print(sent.isalpha())

sent = input("type a string: ")
symbol_checker(sent)


# Try/except understanding program
try:
	x = 5
	#print(int('some_input'))
	a == 8
	#5 + str()
except NameError:
	print("There is Name error occured")
except ValueError:
	print("there is Value error occured")
except TypeError:
	print("there is Type error occured")
except:
	print("Unknown error")
else:
	print("no errors occured")
finally:
	print("Code has done running!")



