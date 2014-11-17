class Animal:
	def __init__ (self, name, age):
		self.name= name
		self.age= age
	def sleep (self):
		print self.name + " of " + str(self.age) + " years old is sleeping"
class Dog (Animal):
	def __init__ (self, fur_color, name, age):
		Animal.__init__(self, name, age)
		self.fur_color= fur_color
	def bark (self):
		print self.name + " with fur colour " + str(self.fur_color) + " is barking"
		
a= Dog("brown", "bob", 77)
a.sleep()
