#Author: 
#Date:


def countStudentClass(studentScore_list):
	if len(studentScore_list) < 1:
		print("Please add at least 1 item into the list")
		return 0
	
	nerdCount_list = [0] * 7  #intialize the output list
	
	#Please write your own program here

	
	
	return nerdCount_list	
	
	
if __name__ == '__main__':

	#test cases
	#studentScore_list = []  #
	studentScore_list = [23, 76, 1300, 600]   #output should be [0, 0, 2, 0, 1, 1, 0]

	try:
		print(countStudentClass(studentScore_list))
	
	except e:
		print(e)
		raise	