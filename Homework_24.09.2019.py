#the odd or even number checker programm
The_number=int(input('write the number: '))
(The_number%2==0 and print('the number is even')) or (The_number%2!=0 and print('the number is odd'))

#circle area calculator programm
radiusofcircle=float(input('insert the radius of circle: '))
area=3.14*radiusofcircle**2
print('the circle area is', area)

#shows current date and time programm
import datetime
print('Current date and time :')
print(datetime.date.today())