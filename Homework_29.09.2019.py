#any number multiplication table program
number = int(input("please insert a number: "))
for i in range(1, 11):	
		print(number," * ",i," = ",number*i)

# pattern build program			
for i in range(1,7):
	if i <= 5:
		print("* " *i)
	else:
		for j in range(4,0,-1):
			if j >= 0:
				print("* " *j)

# Digit(s) counter in number
count = 0
while (number > 0):
	number = number//10
	count+=1
print("There are ", count, "digit(s) in the inserted number")
