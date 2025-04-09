from random import randint
from numbers import number_list, logo
    

#pick the random number
number_random= randint(1,100)
# print(number_random)

print(logo)
print('Welcome to the Number Guessing Game')
print('I\'m think in a number between 1 and 100 🤫')

difficult= input('choose a difficulty.Type \'easy\' or \'hard\' to play: ' ).lower()

LIFE=0

if difficult == 'easy':
    LIFE=10
    print("Okay! You have 10 attempts")

else:
    LIFE=5
    print("Okay! You have 5 attempts")

attempts= True

while attempts:
    user_tentative = int(input ("Make a guess:\n"))
   
    if  LIFE == 1:
        print("You've run out of guesses. Refresh the page to run again.☠️")
        attempts=False
    
    elif user_tentative > number_random:
        LIFE -=1
        print ("Too high \n Guess again.")
        print (f'{LIFE} attempts remaining to guess the number')
        
    elif user_tentative < number_random:
        LIFE -=1
        print ("Too low \n Guess again.")
        print (f'{LIFE} attempts remaining to guess the number')
      
    else:
        print('Congratulation!! You win!')
        attempts=False
        exit()
     