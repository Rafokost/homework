'''Somebodys_name = input('Tell your name ')
Somebodys_age = input('Tell your birth year = ')
Somebodys_age = int(Somebodys_age)
x=Somebodys_age+100-2019
print('you will be 100 years old after',x)'''

'''x=int(input('the first edge = '))
y=int(input('the second edge = '))
z=int(input('the third edge = '))

(((x+y>z and x+z>y) and y+z>x) and print('tringle is possible')) or ((x+y<=z or x+z<=y or y+z<=x) and print('tringle is impossible'))'''


'''x = int(input("input the first number "))
y = int(input("input the second number "))
z = int(input("input the third number "))


if x %2 ==0 and y %2==0 and z %2==0:
	print("the whole input numbers are even")

if x %2 !=0 or y %2!=0 or z %2!=0:
	print('not all the input numbers are even',x,y,z)

weather = input('weather condition ')
if weather == 'cold':
	mydress = input('how to dressed ')
	if mydress == 'short':
		print('wear the jacket')
	elif mydress == 'long':
		print('you feel good')
	else:
		print('input parameters error')
	 	
else:
	print('there is sunshine weather outside')

number = int(input('the number: '))
if number<0:
	print('the number is negative')
elif number == 0:
	print('the number is zero')
else:
	print('the number is positive')


temp = int(input('temp of frozen cell: '))
if temp**2//2 <= 40:
	power = temp*100-142
	print('needed input power in Watts is: ',power)
elif temp**2//2 >= 70:
	power = temp*100//4
	print('there is no auxilary power',power)
else:
	print('Karno cycle is working')


sum = 0
x = int(input("Enter needed number quantity: "))
for  i in range(1,x+1):
	next_number = int(input("Enter number # " + str(i) + ": "))
	sum += next_number
print(sum/x)

some_string = "hello world"
for i in some_string:
	print(i)

import random
hidden_number = random.randint(1,100)
user_guess = 0
while not user_guess == hidden_number:
	user_guess = int(input("Guess a number: "))
	if user_guess > hidden_number:
		print("Too high!")
	elif user_guess < hidden_number:
		print("Too low!")
	else:
		print("Thats right!")


for i in range(1,4):
	for j in range(1,5):
		print(i,"times",j, "equal", i*j)


for i in range(0,12):
	if i % 2 !=0:
		pass
	else:
		print(i)

def add_to_numbers(num1, num2):
	return num1 + num2

first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))


print(add_to_numbers(first_number,second_number))

def print_hello_world():
	print("Hello World")

print_hello_world()


def mini_prog(x,y,z):
	count = 0
	print(range(x,y,z))
	for i in range(x,y,z): 
		if x>0 and z!=0:
			count+=1
	return count
x = int(input())
y = int(input())
z = int(input())

print(mini_prog(x,y,z))

def even_or_odd(number):
	if number % 2 == 0:
		return "Even"
	return "odd"
x = int(input("Enter number: "))
print(even_or_odd(x))


def two_numbers(num1,num2):
	x = num1**num2
	return x
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
print(two_numbers(num1,num2))


def currency_amount(amount, currency):
    amount = str(amount)
    if currency == "JPY":
        return "¥" + amount
    elif currency == "USD":
        return "$" + amount    
    elif currency == "EUR":
        return "€" + amount
    else:
        return amount
print(currency_amount(5, "JPY"))


def check_balance(price_of_item,user_balance):
	tax = price_of_item * 0.3
	if (price_of_item + tax) < user_balance:
		print ("You can buy the needed item")
	else:
		print("Your sellary is low try work harder")

price_of_item = int(input("Enter price_of_item = "))
user_balance = int(input("Enter user_balance = "))

check_balance(price_of_item,user_balance)
_________________________________
ameria = "0001"
convers = "0002"
ineco = "0003"
evoca = "0004"
american_express = "0005"

balance = 500

def check_balance(purchase_price):
	if purchase_price > 0:
		return "You have not enough balance"
	elif purchase_price <= balance
	else:
		return "Your balance after purchase is" + str(purchase_price - balance)

def validate_credit_card(card_number):
	if len(card_number) == 16 and card_number[0:4] != american_express:
		return True
	elif len(card_number) == 15 and card_number[0:4] == american_express:
		return True
	else:
		return False

def check_card_bank(card_number):
	if card_number[0:4] == ameria:
		return "Ameria Bank"
	elif card_number[0:4] == convers:
		return "Evoca Bank"
	elif card_number[0:4] == ineco:
		return "Ineco Bank"
	elif card_number[0:4] == evoca:
		return "Evoca Bank"
	else:
		return "American Express Bank"

card = input("Enter your card number: ")

if validate_credit_card(card):
	print("Your credit card belongs to " + check_card_bank(card))
	purchase = 501
	while check_balance(int(purchase)) == "You have not enough balance" or check_balance(int(purchase):
		purchase = input("Enter your purchase price") 
	input("Enter your purchase price")
	print(check_balance(int(purchase)))
else:
	print("You've entered wrong credentials")






try:
	print()/5
	print("hi")
except:
	print("error occured")

ms = "This string is not a number!"

try:
	print("Converting my string to int...")
	print("String #" + "1" + ": " + ms)
	my_int = int(ms)
	print(my_int)
except ValueError:
	print("Can't convert; ms to a number")
except TypeError:
	print("Can't concatianate number with string")
except:
	print("Unknown error")
else:
	print("no errors occured")
print("Done")

try:
	input_file = open("NumberFile.txt", mode = "r")

	try:
		for line in inpute_file:
			print(int(line))
	except ValueError:
		print("A value error occured")

	else:
		print("No errors occured")

	finally:
		input_file.close()

except IOError:
	print("An error occured reading the file!")


def zero_division():
	print(1/0)

try:
	zero_division()
except Exception as error:
	print(error)



while True:
	try:
		x = int(input("Enter a number"))
		y = int(input("Enter another number"))
		print(x, "/", y, "=", x/y)
		break
	except ZeroDivisionError:
		print("Can't divide by zero")
	except ValueError:
		print("That does not look like a number!")
	except:
		print("Something unexpected happened")

	
# id explanation
my_int = 14
print(id(my_int))
# is conected id explanation
print(5 is 6)
print(id(5) == id(6))

# chr working
print(chr(85))
# ord working
print(ord("!"))

text = input("Enter text:\n ")
count = 0
for i in text:
	if ord(i) == ord("!"):
		count += 1
print("The count of ! is: ", count)

#slicing string
print(text[0])
print (text[0:5])

# find operator
print(text.find("g"))
print(text.find("j", 2,8))

# Split 
print(text.split(" "))
print(text.capitalize())
print(text.lower())
print(text.upper())

print(text.replace("gh", "changed"))
print(text.title())


# lesson work
def get_middle_three_chars(sample_str):
	middle_index = int(len(sample_str)/2)
	print("Original string is", sample_str)
	middle_three = sample_str[middle_index - 1:middle_index + 2]
	print("Middle three chars are", middle_three)

print(get_middle_three_chars("JhonDipPeta"))
print(get_middle_three_chars("Jasonayh"))

________________
a = (1,2)
print(a)
print(a[0], a[1])

def tuple1():
	un = input("Enter your name ")
	us = input("Enter your surname ")
	return un, us

ui = tuple1()
print("Your name is " + ui[0])
print("Your surname is " + ui[1])


nested_tuple = ((1,2), (3,4), (5,6))
print(nested_tuple[0])
print(nested_tuple[0][0], nested_tuple[1][0])


my_list = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21 ,22,23]

my_list.remove(23)
print(my_list, ": After removing 23")

my_list.sort()
print(my_list," :After sorting")

my_list.reverse()
print(my_list," :After reversing")

my_list.pop()
print(my_list, " : poping")

del my_list[-5:]
print(my_list, ": After deleting the last five items")



my_list = [1, 2, 3, 4]

my_list.append(5)
print(my_list, ": After appending five")

new_list = [6,7,8]
my_list.extend(new_list)
print(my_list, ": After extending")

my_list.insert(0, 0)
print(my_list, ": After inserting zero")

def average(in_list):
	sum = 0
	for number in in_list:
		sum += number
	return sum / len(in_list)

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [88, 55 ,68 ,54 ,25 ,1 ,2 ,78]

print("The average of my_list is: ", average(my_list1))
print("The average of my_list2 is: ", int(average(my_list2)))


def two_D_average(in_2d_list):
	result = []

	for num_list in in_2d_list:
		sum = 0
		for number in num_list:
			sum += number
		result.append(sum // len(num_list))

	return result

my_2d_list = [[61,32,12,123],[123,131,131,123],[4,1,2]]
print("average:", two_D_average(my_2d_list))


l1 = [52,45,45,78,100,64,28,100,100,1,0]
big = 0
for i in l1:
	if i > big:
		big =i
print(big)





mint1 = 1
mint2 = 2
mint3 = 3

out_put_file = open("OutputFile.txt", "w")

out_put_file.write(str(mint1))
out_put_file.write(str(mint2))
out_put_file.write(str(mint3))

out_put_file.close()


myintlist = ["gfh","gtt","tyu","eew","yuy"]

out_put_file = open("OutputFile.txt", "w")
for line in myintlist:
	out_put_file.write(line)

out_put_file.close()


myintlist = ["gfh","gtt","tyu","eew","yuy"]

out_put_file = open("OutputFile.txt", "w")
out_put_file.writelines(line)
out_put_file.close()


myintlist = ["gfh","gtt","tyu","eew","yuy"]

out_put_file = open("OutputFile.txt", "a")

for i in range(len(myintlist)):
	myintlist[i] += "\n"

	out_put_file.writelines(line)
out_put_file.close()

myintlist = ["gfh","gtt","tyu","eew","yuy"]

out_put_file = open("OutputFile.txt", "r")

print(out_put_file.readline())
print(out_put_file.readline())

out_put_file.close()

names_list = []
out_put_file = open("OutputFile.txt", "r")

for line in out_put_file:
	names_list.append(line)

out_put_file.close()
print(names_list)


p = int(input("Enter a number of list's carachter: "))
list1 = []
for i in range(p):
	string = input("Enter a string: ")
	list1.append(string)

def new_list_creator(listik,n):
	list2 = []
	for i in listik:
		print(i)
		if len(i) >= n:
			list2.append(i)

	return list2

listik = ["dfgsdf","sdfgsdf","dfg","hh"]
n = int(input("Enter : "))
print(new_list_creator(listik,n))

list_5 = []
def list_character_place_changer(list_new):
	count = 0
	for i in list_new:
		count += 1
		print(i)
		if count == 1:
			list_new.insert(3,i)
			list_new.remove(0,i)
		elif count == 2:
			list_new.insert(4,i)
			list_new.remove(2,i)
	return list_new

list_new = ["uiy","kjhfg","kjhf","hh","yiui"]
print(list_character_place_changer(list_new))



human = {"name":"High","Temperature":"Low","number": 15}

print(human["number"])
print(human)
print(human["name"], human["Temperature"])

human["number"] = 30


human["have_pet"] = False
print(human)

del human["name"]
print(human)

print(human.keys())
print(human.values())

for value in human.values():
	print(value)


fruits = {"apple": 5, "orange": 14, "bananas": 4,"pomegranade":8}

for key in fruits.keys():
	if fruits[key] > 5:
		print(key)

print(fruits.items())

for (name,kg) in fruits.items():
	print(name, "is", kg, "In store")

# marks = {"Gor Smbatyan": 26,"David Grigoryan": 26,"Vardges Hovhannisyan":26, "Rafayel Kostanyan": 28,"Mehrabyan Shahen": 30 }
# print(marks)

# marks["David Grigoryan"] = 15

# print(marks)

classes = {"Math":["David","Lucy","Dana"],"Physics": ["Addision", "Benjamin"],
"Chemistry": ["Sara", "Pele"]}

print("Students in math class", classes["Math"])
classes["Math"].append("Jirayr")

print("Students in math class", classes["Math"])


people = {"Dany":{"Age": 24, "is married": False}, "Diana":{"Age": 32, "is married": True}}
print(people.keys())
print(people.values())

sample_text = "a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses"

words_dict = {}

sample_text = sample_text.lower()
sample_text = sample_text.replace(",","")
sample_text = sample_text.replace(".", "")
sample_text = sample_text.split(" ")

for word in sample_text:
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict[word] = 1


for (word, amount) in words_dict.items():
	if amount > 1:
		print(word, ":", amount)'''

# objects

class Person:
	def __init__(self):
		self.first_name = "[no first name]"
		self.last_name = "[no last name]"
		self.eye_color = "[no eye color]"


my_person = Person()

print(my_person.first_name)
print(my_person.last_name)
print(my_person.eye_color)



class Name:

	def __init__(self):
		self.first_name = "[no first name]"
		self.last_name = "[no last name]"

class Person:

	def __init__(self):
		self.name = Name()
		self.eye_color = "[no eye color]"


my_person = Person()

print(my_person.name.first_name)
print(my_person.name.last_name)
print(my_person.eye_color)


# Encupsulating

class Person:

	def __init__(self,first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.eye_color = "[no eye color]"


my_person = Person("Jirayr", "Melikyan")

print(my_person.first_name)
print(my_person.last_name)
print(my_person.eye_color)


#class realization example

class BankAccount:
	def __init__(self,name, balance = 0.0):
		self.log("Account created!")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("Balance checked at " + str(self.balance))
		return self.balance

	def deposit(self,amount):
		self.balance += amount
		self.log("+" + str(amount) + ": " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + "+ " + str(self.balance))

	def log(self,message):
		print(message)


my_bank_account = BankAccount("Jirayr Melikayn")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()