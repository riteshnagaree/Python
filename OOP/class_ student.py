class Student:
	def __init__(self,student_id,name):
		self.name=name
		self.student_id=student_id

	def add_results(self,subject,score):
		self.subject=subject
		self.score=score

	def get_results(self):
		return self.results

	def __str__(self):
		return f"Student ID: {self.student_id}, Name: {self.name}"

class Result:
	def __init__(self,subject,score):
			self.subject=subject
			self.score=score

	def __str__(self):
		return f"Subject: {self.subject}, Score: {self.score}"


student1=Student(1,"Alice")
student1.add_results("Math",95)
student1.add_results("Science",88)


print(str(student1))
for result in student1.get_results():
	print(result)