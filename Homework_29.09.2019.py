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
