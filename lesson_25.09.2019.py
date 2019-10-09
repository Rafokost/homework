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
print(get_middle_three_chars("Jasonayh"))'''


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
