# number_comparison_checker program
def number_comparison_checker(number_1,number_2,number_3):
	if number_1 > number_2 and number_1 > number_3:
		print("The first number is Max")
	elif number_2 > number_3 and number_2 > number_1:
		print("The second number is Max")
	elif number_3 > number_2 and number_3 > number_1:
		print("the third number is Max")
	else:
		print("Inputed numbers are equil!")

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
number_comparison_checker(number_1,number_2,number_3)

# "FizzBuzz" program
def fizz_buzz(inputed_number):
	if inputed_number % 5 != 0 and inputed_number % 3 == 0 :
		print("Fizz")
	elif inputed_number % 3 != 0 and inputed_number % 5 == 0 :
		print("Buzz")
	elif inputed_number % 3 == 0 and inputed_number % 5 == 0 :
		print("FizzBuzz")
	else:
		print(inputed_number)

inputed_number = int(input("Enter a number: "))
fizz_buzz(inputed_number)

# In the inputed range Odd/Even numbers finder program
def showNumbers(limit):
	for i in range(0,limit+1):
		if i % 2 == 0:
			print(i,"Even")
		else:
			print(i, "Odd")

limit = int(input("Number range from 0 to "))
showNumbers(limit)


