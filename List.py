numberList = [5,1,3,4,2]

sumOfNumberList = 0 
for x in numberList:
  sumOfNumberList = sumOfNumberList + x 
 


print (sumOfNumberList)  

lenghtOfList = len(numberList)   
averageOfNumberList = sumOfNumberList / lenghtOfList
print(averageOfNumberList) 
#printe alles größer 3.
sumOfNumberList = 0 
for x in numberList:
 sumOfNumberList = sumOfNumberList + x 
 if sumOfNumberList > averageOfNumberList:
   print(sumOfNumberList) 