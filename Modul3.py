import os 
os.system("cls")

"""
#1. Skriv ut något som användaren skriver in 10 gånger med kommandon input() & for loop
amount = int(input("Write 10 as your amount: ")) 

for i in range (0,amount): 
    print("Hello world") 

#2. Skriv ut samtliga heltal mellan 1 och 10
for x in range (0,10):
    print(str(x+1))
 
#3. Skriv ut samtliga heltal mellan 1 och y
y = int(input("Write amount: ")) 

for i in range (0,y): 
    print(str(i+1)) 

#4. Gör ett program som skriver ut gångertabeller med nästlade for-loopar
for x in range(1, 10):
    for y in range(1, 10):
        print("%s * %s" %(x, y), end = "\t")
"""

#5. 5. FRIVILLIG: Skapa ett program som manuellt (ej med **) upphöjer ett tal med for-loop

user_number = int(input("Type in a number you want to inpower "))

user_inpower = int(input("Type in how many times you want to inpower your number "))

result = user_number

for x in range (1, user_inpower): 
        result = user_number * result
print(result)