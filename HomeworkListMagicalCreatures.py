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
