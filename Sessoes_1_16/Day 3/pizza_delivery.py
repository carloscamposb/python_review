 #Pizza Deliveries

print("Welcome to pizza deliveres")
size= input("What size of pizza do you want? S/M/L: \n")
pepperoni=input("Would you like to add pepperoni? Y or N: \n")
extra_cheese= input("Do you wanna extra cheese on your pizza? Y or N: \n") 

value=0

if size == 'S':
    value+=15
elif size=='M':
    value+=20
elif size =='L':
    value+=25
else:
    print('error')

if pepperoni =='Y':
    if size == 'S':
        value+=2
    else:
        value+=3    
          
if extra_cheese =='Y':
    value+=1   
else:
    value       

print(f"Your final bill is: ${value}")            



