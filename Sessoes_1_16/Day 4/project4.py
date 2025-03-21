#Rock paper and Scissors
import random

list=['Rock', 'Paper', 'Scissors']

choice= int(input("What is your choice? \n"
             "Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))




print(f'Personal choice: {list[choice]}')
   

computer_choice= random.randint(0,2)

print(f'Computer choose: {list[computer_choice]}')



# Rock < Paper < Scissors < Rock 

if list[computer_choice] == 'Rock' and list[choice] =='Rock':
    print ('Draw')

elif list[computer_choice] == 'Rock' and list[choice] =='Paper':   
    print ('You won!')

elif list[computer_choice] == 'Rock' and list[choice] =='Scissors':   
    print ('You lose!')    

elif list[computer_choice] == 'Paper' and list[choice] =='Paper':   
      print ('Draw')

elif list[computer_choice] == 'Paper' and list[choice] =='Scissors':   
    print ('You won!') 

elif list[computer_choice] == 'Paper' and list[choice] =='Rock':   
    print ('You lose!') 

elif list[computer_choice] == 'Scissors' and list[choice] =='Scissors':   
        print ('Draw')

elif list[computer_choice] == 'Scissors' and list[choice] =='Paper':   
    print ('You won!') 

elif list[computer_choice] == 'Scissors' and list[choice] =='Rock':   
    print ('You lose!') 

