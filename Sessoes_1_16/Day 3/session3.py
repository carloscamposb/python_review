# if/else statements
# if condition:
#     do this
# else:
#     do that

#about the height
height=int(input("what is your height in cm?"))

if height >= 120:
    print("You can ride the rollecoaster ") #avoid indentationError
else:
    print("Sorry you need to be taller before you can ride.")    


#Operators:
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != No equal to


#Module (%)
# 10%5=2
# 10%3=1

number= int(input("Choose a number and I'll say if is even or odd: "))

if number%2==0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")    


#Nesting and elif
#Multiple conditions  

height=int(input("what is your height in cm?"))

bill=''

if height >= 120:
    print("You can ride the rollecoaster ")
    age=int(input("what is your age?"))
    if age <= 12:
        bill=5
        print("child, pay $5 dollars") 
 
    elif age <=18:
        bill=7
        print("young, pay $7 dollars")       
    elif age >=19: 
        bill=12
        print("adult, pay $12 dollars")
    elif age >=45 and age <=55:
        print("You don't need to pay")
    else:
        print("Check your age again. Have a free ride on us!")    
    photos=input("Do you wanna photos? We add $3 dollars: yes or no? \n") #This condition appers independent of the previus answers

    if photos == 'yes':
        new_bill = bill +3
        print(f"In addition you won't pay {bill}, now is {new_bill } \n")
    else:
        print(f"Ok your bill is {bill}")

else:
    print("Sorry you need to be taller before you can ride.")  

  
#Logical Operators:
#  and , or , not

 