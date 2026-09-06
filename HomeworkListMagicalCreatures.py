sparkle_counts = [23,58,31,77,85,49,92,38,67,55]

sumOfsparkle_counts = 0 
for x in sparkle_counts:
  sumOfsparkle_counts = sumOfsparkle_counts + x 
print("Die Gesamtanzahl an Sparkles ist " + str(sumOfsparkle_counts)) 
  
lenghtOfList = len(sparkle_counts)   
averageOfsparkle_counts = sumOfsparkle_counts / lenghtOfList
print("Die Durchschnittliche Anzahl an Sparkles ist " +str(averageOfsparkle_counts))

sparkle_counts.sort() 
print("Die maximale Anzahl an Sparkles ist " + str(sparkle_counts[len(sparkle_counts) - 1]))
print("Die minimale Anzahl an Sparkles ist " + str(sparkle_counts[0]))
print()
print("Folgende Sparkles sind größer als der Durchschnitt an Sparkles:") 

for x in sparkle_counts:
 if x  > averageOfsparkle_counts:
   print(x) 
print()

print("Folgende Sparkles sind Mitglieder der Twilight Glow Gruppe:") 
for x in sparkle_counts:
 if x  >= 40 and x <= 70:
   print(x) 
print()

myFloat = 1.0 
myInt = int(myFloat) # Typecasting  
myList = [5,3,4,2,1]
myListAufsteigend = [] 

#Aufsteigend 

for i in range(len(myList)): 
  if i == 0: 
   myListAufsteigend.append(myList[0])
  else:
   for j in range(len(myListAufsteigend)):
    if myList[i] < myListAufsteigend[j]: #3 < 5
     myListAufsteigend.insert(j, myList[i])
     break 
   else:
    myListAufsteigend.append(myList[i])
    j+1
  i+1  
print(myListAufsteigend) 
#   myListAufsteigend.insert(1,myList) 
# Absteigend
myListAbsteigend = []

for i in range(len(myList)): 
  if i == 0: 
   myListAbsteigend.append(myList[0])
  else:
   for j in range(len(myListAbsteigend)):
    if myList[i] > myListAbsteigend[j]: #3 < 5
     myListAbsteigend.insert(j, myList[i])
     break 
   else:
    myListAbsteigend.append(myList[i])
    j+1
  i+1  
print(myListAbsteigend) 








# Ausgangsituaton myListAufsteigend ist leer.
# Erster Durchlauf = Index 0  myListAufsteigend wir befüllt  
# Zweiter Durchlauf = Index 1  Wenn myList[i] > myListAufsteigend[i-1]