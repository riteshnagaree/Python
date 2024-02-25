class Students:
	def __init__(self,name,age,student_id):
		self.name=name
		self.age=age
		self.student_id=student_id
		self.subjects=["Programming technologies","Embedded Linux"]
	def info(self):
		print(self.name,"is studying in",self.subjects[0])

student1=Students("Tatya",21,3)
print(student1.name)

student2=Students("Kakya",43,20)
student2.info()
