#Author: 
#Date:


def countStudentClass(studentScore_list):
	if len(studentScore_list) < 1:
		print("Please add at least 1 item into the list")
		return 0
	
	nerdCount_list = [0] * 7  #intialize the output list
	
	#Please write your own program here
	for studentscore in studentScore_list:
		if (studentscore < 1):
			nerdCount_list[0] += 1
		elif (studentscore < 10):
			nerdCount_list[1] += 1
		elif (studentscore < 100):
			nerdCount_list[2] += 1
		elif (studentscore < 500):
			nerdCount_list[3] += 1
		elif (studentscore < 1000):
			nerdCount_list[4] += 1
		elif (studentscore < 2000):
			nerdCount_list[5] += 1
	
	
	return nerdCount_list	
	
	
if __name__ == '__main__':

	#test cases
	#studentScore_list = []  #
	studentScore_list = [23, 76, 1300, 600]   #output should be [0, 0, 2, 0, 1, 1, 0]

	try:
		print(countStudentClass(studentScore_list))
	
	except Exception as e:
		print(e)
		raise	