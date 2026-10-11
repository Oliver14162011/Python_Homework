class Animal:
 def __init__(self,name,species):
  self.name = name
  self.species = species

 def speak(self):
  print("Some generic animal sound.")

class Dog(Animal):
 def speak(self):
  print("Woof!")

class Cat(Animal):
 def speak(self):
  print("Meow!") 



c = Animal("Snoopy","Dog") 
c.speak() 
x = Dog("Snoopy","Dog") 
x.speak()
y = Cat("Garfield","Cat") 
y.speak() 