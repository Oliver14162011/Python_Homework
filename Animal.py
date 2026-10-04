class Animal:
 def __init__(self, name, age, species): 
  self.name = name
  self.age = age
  self.species = species

 def introduce(self):
   print(f"I am a {self.species}.")  
   print(f"My name is {self.name}.")
   print(f"I am {self.age} years old.") 
 def makeSound(self):
  if self.species == "Dog":
   print("Wuff!") 
  if self.species == "Bird":
   print("Tweet!")
  if self.species == "Cat":
   print("Miau!")
  print()   

dog = Animal("Snoopy",2,"Dog")
bird = Animal("Woodstock",3,"Bird")
cat = Animal("Garfield",6,"Cat") 

dog.introduce()
dog.makeSound()
bird.introduce()
bird.makeSound()
cat.introduce() 
cat.makeSound() 