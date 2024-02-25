


student_records = {}


#func to accept and store a student record
def add_student_record():
	student_id = input("Enter the student id: ")
	name=input("Enter the name: ")
	grade=input("Enter the grade: ")
	student_records[student_id] = {'Name':name , 'Grade':grade}
	print("Student record added succesfully! ")


# #calling 3 times
# add_student_record()
# add_student_record()
# add_student_record()





def display():
	if student_records:
		print("Student records: ")
		for student_id,record in student_records.items():
			print(f"Student_id: {student_id}")
			print(f"Name: {record['Name']}")
			print(f"Grade: {record['Grade']}")
			print("---------------------------")
	else:
		print("No student record found")

add_student_record()
add_student_record()
add_student_record()

display()