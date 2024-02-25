class student:
	def __init__(self,name,age,student_id):
		self.name = name
		self.age = age
		self.student_id = student_id
		self.subjects = ["DSA","OS"]

	def display_info(self):
		print("Name : {self.name}")
		print("Age : {self.age}")
		print("Student Id : {self.student_id}")
		print("Subject : {self.subjects}")

class AIstudent:
	def __init__(self,name,age,student_id,specialization):
		super.__init__(name,age,student_id)
		self.specialization = specialization
		self.subjects += ["Python","machine learning"]

	def display_info(self):
		super().display_info()

		print("specialization: {self.specialization}")
		print("Field : Artificial Intelligience")	


class ProgrammingStudent:
	def __init__(self,name,age,student_id,specialization):
		super.__init__(name,age,student_id)
		self.specialization = specialization
		self.subjects += ["Java","C++"]
		self.batch = "morning"

	def display_info(self):
		super().display_info()

		print("specialization: {self.specialization}")
		print("Field : Programming")
		print("batch : {self.batch}")



ai_student = AIstudent("Alice",20,"AI123","Machine learning")

programming_student = ProgrammingStudent("Bob",22,"Prog123","Web Programming")



ai_student.display_info()
print()
programming_student.display_info()
print()

