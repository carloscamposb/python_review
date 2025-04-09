import random
from cards import cards_values, logo_game


    # ======== Functions =========
def subst(num1:int, num2:int) -> int:
        '''This function performs subtractions.'''
        return num1 - num2

def sum_cards(num1:int,num2:int) -> int:
        '''This function sum the values.'''
        return num1 + num2

def last_number(calculation:int, num3:int) -> int:
        '''This function add one more number and sum'''
        return calculation + num3

def verification(calculation:int, new_calculation:int, calculation_dealer:int)->int:
        '''This function checks for victory and defeat'''
        if calculation == calculation_dealer:
            return 'Oh no! It\'s a draw! 👀'
        
        elif calculation >21 or new_calculation>21:
            return 'You went over. You lose ☠️'
        
        elif calculation_dealer > 21:
            return 'Congrats! You win 🎉✨'
        
        elif calculation == 21 or new_calculation ==21:
            return 'Congrats! It\'s a Blackjack. You won! 🎉✨'
        
        elif calculation_dealer ==21:
            return 'You went over. The computer made a Blackjack. You lose ☠️'
        
        elif calculation > calculation_dealer:
            return 'Congrats! You win 🎉✨'
        
        else:
            return 'You went over. You lose ☠️'    

while True:
    # ============ User===========

    print(logo_game)
    
    cards_user=random.choices(cards_values,k=2)
  
    values_save= {
        'card1': cards_user[0],
        'card2': cards_user[1],
    }

    calculation=0
    new_calculation=0
    calculation_dealer=0

    
    num1=values_save['card1']
    num2=values_save['card2']
    calculation= sum_cards(num1, num2) 

    print(f'your cards: {num1} and {num2}, current score: {calculation}')

    if  values_save['card1'] == 11 or values_save['card2'] == 11:
        decision= input("Do you wanna transform the number 11 in number 1? y/n: \n")
        if decision == 'y':
            values_save['card1']=subst(11,10)
            print(f'New hand: {values_save}, current score: {calculation}')

    # ======== dealer =======
    
    cards_dealer=random.choices(cards_values,k=2)

    values_save_dealer= {
        'card1': cards_dealer[0],
        'card2': cards_dealer[1],
    }

    
    num3=values_save_dealer['card1']
    num4=values_save_dealer['card2']
    calculation_dealer= sum_cards(num3, num4) 


    print(f'Dealer\'s first card: {values_save_dealer['card1']}')

    # ========== Results =============

    choice=input("Type 'y' to get another card, type 'n' to pass: \n").lower()

    if choice == 'n':
        print(f'Your final hand: {num1} and {num2}, final score:{calculation} ')
        print(f'Dealer\'s final hand: {num3} and {num4}, final score:{calculation_dealer}')
        print(verification(calculation,0, calculation_dealer))

    else:
        cards_user+=random.choices(cards_values,k=1)
        values_save['card3']=cards_user[0]
        num3=values_save['card3']
        new_calculation=last_number(calculation, num3)
        print(f'Your final hand: {num1}, {num2} and {num3}, final score:{new_calculation}')
        print(f'Dealer\'s final hand: {num3} and {num4}, final score:{calculation_dealer}')
        print(verification(0,new_calculation,calculation_dealer))

    replay=input('Do you wanna play again? y/n: \n').lower()

    if replay == 'n':
        print("Ok! Thank you! 😉")
        break         
    else:
        print('\n'*20)