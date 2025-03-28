import random
import hangman_words
# I can use from hangman_words import logo,things,character

print(hangman_words.logo)



name_random=random.choice(hangman_words.things).lower()
print(name_random)

placeholder=''
game_over=False
check=[]
lives=7


for name in name_random:
    placeholder += "_ "
print(placeholder)    


while not game_over:
    guess=input("Guess a letter: \n").lower() 
    display=""
   
    for name in name_random:
        if guess in check:
            print(f"You've already used this letter: {guess}")
        else:
            print(f"You found a letter: {guess}")    
        if guess==name:
            display+= name
            check.append(name)
        elif name in check:
            display+=name  
        else:
            display+='_'
 
    print(display)      
       
    if guess not in name_random:
        lives-=1
        print(f"the letter {guess} is not in this word")
        print(f"You lost a life. Now you just have {lives}")
        if lives == 0:
            game_over=True
            print("\nYou lost ☠️") 
            print(f"The correct answer is {name_random}")
    
    if '_' not in display:
        game_over=True
        print("\nYou win ✨🎉") 

    print(hangman_words.character[lives])    

