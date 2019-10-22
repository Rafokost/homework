
# class exercise N 1

class String:
	def __init__(self,name):
		self.name = name
		
	def get_string(self):
		self.name = input("Put your string here: ")

	def print_string(self):
		name = self.name.upper()
		print(name)

the_answer = String("")

the_answer.get_string()
the_answer.print_string()


# class exercise N 2

class vehicle:
	def __init__(self,color):
		self.color = color


	def car1(self):
		if self.color == "red":
			name = "FER"
			price = "60.000$"
			print("The name of the car is: ",name,"\n","The price of the car is: ",price)
		

	def car2(self):
		if self.color == "blue":
			name = "JUMP"
			price = "10.000$"
			print("The name of the car is: ",name,"\n","The price of the car is: ",price)
				

	def colour(self):
		if self.color != "red" and self.color !="blue":
			print("There is no car in the data with such color")


vehicle_finder = vehicle(input("Put the disarable vehicle color here: "))

vehicle_finder.car1()
vehicle_finder.car2()
vehicle_finder.colour()
