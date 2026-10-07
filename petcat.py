class PetCat:
 def __init__(self,mood):
  self.__mood = mood

 def __updateMood(self,action):
  if action == "pet":
   self.set_mood("sleepy")
  if action == "feed":
   self.set_mood("happy") 
  if action == "ignore":
   self.set_mood("grumpy")

 def getMood(self):
  return self.__mood
 
 def setMood(self,mood):
  if mood != "":
   self.__mood = mood

 def interact(self,action):
  self.__updateMood(action)
 

cat = PetCat("grumpy")
cat.interact("pet")     

print(cat.getMood()) 


