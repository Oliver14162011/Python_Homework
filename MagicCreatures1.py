class MagicCreatures:

 MIN_WEIGHT = 10 # Unveränderbar, für die ganze Klasse gültig, auch für jedes Objekt gültig
 MAX_WEIGHT = 500
 MAX_AGE = 20
 GRASS_FOR_MAGIC = 4.0
 WATER_FOR_MAGIC = 3.0

 magic_price = 1.0 #Veränderbar, für die ganze Klasse gültig, für jedes Objekt gültig

 def __init__(self,name,weight,birth_year):
  self.name = name
  self.weight = weight
  self.birth_year = birth_year
  self.eaten_magic_grass = 0 
  self.drank_magic_water = 0
  self.__produced_magic = 0


 def feed_magic_grass(self,amount):
  if amount > 0:
   self.eaten_magic_grass = self.eaten_magic_grass + amount           
  else: 
   print("Error, Amount must be bigger than 0.")

 def drink_magic_water(self,amount):
  if amount > 0:
   self.drink_magic_water = self.drink_magic_water + amount           
  else: 
   print("Error, Amount must be bigger than 0.")

 def __str__(self):
  return f"Name:{self.name},Gewicht:{self.weight},Geburtsjahr:{self.birth_year}"


 def get_produced_magic(self):
  return self.__produced_magic


 def produce_Magic(self):
  max_magic_of_Grass = self.eaten_magic_grass / self.GRASS_FOR_MAGIC
  max_magic_of_Water = self.drank_magic_water / self.WATER_FOR_MAGIC
  self.produced_Magic = min(max_magic_of_Grass,max_magic_of_Water)
  

 def calculate_magic_earnings(self):
  return self.produce_Magic * self.magic_price
  
 














 






