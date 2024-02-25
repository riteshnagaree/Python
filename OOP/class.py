class Person:
	def __init__(self,name,age,subject,marks):
		self.name=name
		self.age=age
		self.subject=subject
		self.marks=marks

	def say_hello(self):
		print("hello, my name is ",self.name," and I am ",self.age,"years old.")

	def marks_student(self):
		print(self.name," got",self.marks,"in ",self.subject)
# Person1 = Person("Nandan",21)
# Person1.say_hello()


# Person2 = Person("Aniket",22)
# Person2.say_hello()

Person3=Person("Kaka",45,"Maths",99)
Person3.marks_student()

