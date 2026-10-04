class PetCat:
 def __init__(self,mood):
  self.__mood = mood 
 def __update_mood(self,action):
  if action == "pet":
   self.set_mood("sleepy")
  if action == "feed":
   self.set_mood("happy") 
  if action == "ignore":
   self.set_mood("grumpy")
 def get_mood(self):
  return self.__mood
 def set_mood(self,mood):
  if mood != "":
   self.__mood = mood
 def interact(self,action):
  self.__update_mood(action)
 

Cat = PetCat("grumpy")
Cat.interact("pet") 

print(Cat.get_mood())


 