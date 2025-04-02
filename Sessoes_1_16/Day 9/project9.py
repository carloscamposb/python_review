informations=True
bid={}
while informations is True:
    name=input("What's your name? \n")
    value=float(input("What's your bid? \nR$"))
    bid[name]=value
    choice=input('Any other bid? (y) / (n): \n').lower()
    if choice == 'y':
        print('\n' *20)
    elif choice == 'n':
        informations=False
    else:
        print('Error. Try again!')

high_bid=0
name_winner=''


for key in bid:
    if bid[key] > high_bid:
        name_winner=key
        high_bid=bid[key]
    elif bid[key] == high_bid:
        name_winner+=' e '+ key
        high_bid=bid[key]
         

print(f'The winner is {name_winner} with a bid of {high_bid}!')
