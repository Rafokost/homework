#space checker program
text = input('Write text here: ')
if " " in text:
	print('there is a space in text')
else:
	print('there in no space in text')

#5 and 11 divisable number checker program
number = int(input("Write number here: "))
if number %5 ==0 and number %11==0:
	print("the input number divisable to 5 and 11")
else:
	print("the input number is not divisable to 5 and 11")

#5 or 11 divisable number checker program
if number %5 ==0:
	print("the input number divisable to 5")
elif number %11 ==0:
	print("the input number is divisable to 11")
else:
	print("the input number is divisable neither 11 nor 5")

#leap year checker program
year = int(input("enter the year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("input year is a leap year")
       else:
           print("input year is not a leap year")
   else:
       print("input year is a leap year")
else:
   print("input year is not a leap year")