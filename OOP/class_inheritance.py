class Animal:
	def __init__(self,name):
		self.name=name

	def speak(self):
		raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
	def speak(self):
		return "woof!"		


class cat(Animal):
	def speak(self):
		return "meow!"		

class Human(Animal):
	def speak(self):
		return "Helloo!"


dog1 = Dog("Johny")
cat1 = cat("Fluffy")
human1 = Human("Charlie")


print(dog1.speak())
print(cat1.speak())
print(human1.speak())

