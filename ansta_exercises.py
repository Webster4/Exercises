import decimal
# Post code counter
# Define funtion with two default prameters
def code_count(c_1 = "89-900", c_2 = "90-155"):

	#Change codes for intiger without dash
	code_int_1 = int((c_1[0:2]+c_1[3:]))
	code_int_2 = int((c_2[0:2]+c_2[3:]))

	#Count difference between ints of codes
	diff = code_int_1 - code_int_2
	diff = abs(diff)

	list_code = [c_1]
	#For loop which generates proper post code to the list
	for i in range(diff):
		#Increasing by 1 code intiger
		code_int_1 +=1
		#Change code for str
		code_str = str(code_int_1)
		#Creating proper post code format
		code_str = code_str[0:2] + "-" + code_str[2:]
		#Statement which ruled out with all zeros in second part xx-000
		if code_str[3:] != "000":
			list_code.append(code_str)

	return list_code


#Parameters for missing_elements function
board = [5, 10, 15, 20, 25, 35, 40, 45, 50]
n = 100
# Function returns missing elements from list in parameter
def missing_elements(board, n):
	elements = []
	
	for i in range(n+1):
		if i not in board:
			elements.append(i)

	return elements

#Function which return list of decimal numbers from range
def decimal_list(x, y, jump):
	num_list = []
	while x < y:
		x += jump
		d = decimal.Decimal.from_float(x)
		num_list.append(d)

	return num_list




def main():
	print("List of post codes")
	print(code_count())
	print("\n\nPrint list from missing_elements funtion")
	print(missing_elements(board, n))
	print("\n\nPrint list of decimal numbers")
	print(decimal_list(2, 5.5, 0.5))

main()
input("\n\n\nPlease press enter to exit the program ")
