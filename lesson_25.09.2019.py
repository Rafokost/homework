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
	print(i)'''

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