# for loop 
n = 6
factorial = n
for counter in range(n - 1):
 #print (counter)
 factorial = factorial * (counter + 1)
 if counter == n - 1: break
print("Die Fakultät von " + str(n) + " lautet: " + str(factorial))

# while loop
counter = 1
factorial = 1
while counter <=n:
 factorial = factorial * (counter)
 counter += 1
print () 
print("Die Fakultät von " + str(n) + " lautet: " + str(factorial))

result = 1
factorial = 6
for i in range(2, factorial + 1):
 result *= i
print(result)