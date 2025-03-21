#Building a tip calculator:

print("Welcome to the tip calculator")
total=float(input("what's the total bill? $"))
tip_quantite= int(input("What percentage tip would you like to give? 10 , 12 or 15? "))
people= int(input("How many people to split the bill? "))

discount=(total*tip_quantite)/100

calculation= round((total+discount)/people,2)

print(f"Each person should pay {calculation}")
