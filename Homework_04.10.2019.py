# Kilometers to miles convert program with a little bit difference program runing steps
'''def kilotomiles(number):
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
(celtofar(temp))'''

#word counter in sentence


def wordcounter(sent):
	count = int()
	b = str()
	letter = int()
	probel = int()
	for i in sent:
		if i !=  " ":			
			letter+=1
		pass
		probel += 1
		if probel - letter == 1:
			count += 1 
	 


	return letter, probel, count

sent = input("Write a sentence: ")

print(wordcounter(sent))