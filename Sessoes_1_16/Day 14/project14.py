from art import logo, vs
import data
import random

def game():
    score = 0
    game_continue = True
    
    # Return the higher value
    def choice_option(option_A, option_B):
        if option_A['follower_count'] > option_B['follower_count']:
            return option_A['follower_count']
        else:
            return option_B['follower_count']    

    # Return the value based on user's choice
    def user_options(user_choice):
        if user_choice == 'a':
            return option_A['follower_count']
        else:
            return option_B['follower_count']
        
    # Game starts here!
    
    option_A = random.choice(data.dados) #readble once

    while game_continue: 
       
        print('\n'*20)
        print(logo)
       
        if score >= 1:   
            print(f'Your current score is: {score} ✨')
            if user_choice =='b':
                option_A=option_B
            else:
                option_A    
        
       
        print(f'🟡 Compare A: {option_A["name"]}, a {option_A["description"]} from {option_A["country"]}.')
        
        # Print the VS graphic
        print(vs)
        
        # Create option B (different from A)
        option_B = random.choice(data.dados)
        while option_B == option_A:
            option_B = random.choice(data.dados)
        
        print(f'🟡 Against B: {option_B["name"]}, a {option_B["description"]} from {option_B["country"]}.')

        # Ask for user input: Who has more followers?
        user_choice = input("Who has more followers? Type 'a' or 'b': ").lower()

        # If correct, increase score and continue
        if choice_option(option_A, option_B) == user_options(user_choice):
            print("You're right! ✨")
            score += 1
        else:
            # If wrong, show final score
            if score >= 1:
                print(f"Sorry, that's wrong. Your final score is: {score} 🪴")
            else:
                print("Sorry, that's wrong! ☠️")
            game_continue = False

game()
