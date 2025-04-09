from random import randint
from numbers import logo

#Global scope
LEVEL_EASY = 10
LEVEL_HARD = 5

# Number
def random_numbers():
    number = randint(1,100)
    return number

num_random= random_numbers()

# print(num_random)

# Difficulty 
def difficulty (choices):
    if choices == 'easy':
        return LEVEL_EASY
    else:
        return LEVEL_HARD
    
def play():
    
    print(logo)
    print('Welcome to the Number Guessing Game')
    print('I\'m think in a number between 1 and 100 🤫')

    choice= input (" Choice a difficult: easy or hard \n").lower()

    life = difficulty (choice) #10 ou 5

    #Compare 
    def compare(num_random, guess, life_game):

        if guess > num_random:
            life_game -= 1
            print("Too high.")
            
        elif guess < num_random:
            life_game -= 1
            print("Too low.") 
        
        else:
            print(f"Congratulations! The number was {num_random} 🎉✨")
            life_game=-1

        if life_game == 0:
            print("It's over! You lost 😢")
            print( f'The number was {num_random}' )
        
        return life_game  


    while life > 0:
        print(f"You have {life} attempts left 👀")
        guess = int(input('Guess a number: \n'))
        life = compare(num_random, guess, life) #update the variable every time to check the aswer
        if life == -1:
            break

play()
   
while input("Do you wanna play again? y/n \n").lower()=='y':
       play()
   




    

 






    


