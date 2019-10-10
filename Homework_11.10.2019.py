# list characters comparison (the first and the last character) checker
def character_comparison(list_of_characters):
	count = 0
	for new_list in list_of_characters:
		for i in new_list:
			character_last = i
			pass
		for j in new_list:
			character_first = j 
			break
		if character_last == character_first:
			count +=1
	return count

List_for_test =  ["abcd", "xyg", "aba","ggg","11221"]
print("The given list is: ",List_for_test)
print("Thers is ",character_comparison(List_for_test),"list's argument which has the same first and last character")

# List empty condition checker program
Empty_list = []
Full_list =  ["abcd", "xyg", "aba","ggg","11221"]
compare_list = []
if Full_list != compare_list:
	print("Inserted list is not empty!")
else:
	print("Inserted list is empty")


# The longest word finder in the list

def longest_word(list_of_characters):
	count = 0
	counted = 0
	for new_list in list_of_characters:
		for i in new_list:
			counted += 1
		if count <= counted:
			a = new_list
			
			count = counted
		counted = 0
	return a

Full_list =  ["hjh","abcd", "xyg", "aba","ggg","1kjhgf11","hj"]
print(longest_word(Full_list))

# The lists members comparison program

def lists_components(list_1,list_2):
	count = 0
	counted = 0
	for new_list_1 in list_1:
		for new_list_2 in list_2:
			if new_list_1 == new_list_2:
				a = True
			else:
				a = False
	return a
			
	
			

list_1 = ["hjh","abcd", "xyig", "aba","ggg","1kjhgf11","hj"]
list_2 = ["dfg","adfgd", "xyg", "adfga","fgg","1kfdggf11","hgj"]
print(lists_components(list_1,list_2))