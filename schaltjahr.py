year = 2099
leap_year = False
if (year % 100 == 0): 
 if (year % 400 == 0): 
   leap_year = True
elif(year % 4 == 0):
   leap_year = True 
#----------------------------------------------------
if leap_year:
 print ("Das Jahr " +str(year) +" ist ein Schaltjahr.")
else:
 print ("Das Jahr " +str(year) +" ist kein Schaltjahr.")
