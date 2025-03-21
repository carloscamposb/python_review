#Treasure Island


print("Welcome to the treasure Island! \n"
      "Your mission is to find the treasure")

# https://ascii.co.uk/art/island
print('''
  

          __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. 
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  |  
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//)
          ':|    "--'(#///)
                      (##///)        
                       \##///\       
                       (###///)       
                       (sjw////)__...--:: :...__
                       (#/::'''                  ""
                  " "'''                          "-._
          __..--""                                      '._
 ___..--""                                                 "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----

''')

choice=input('You\'re  at a cross the road. Where do you wanna go? \n'
             'Type "left" or "right": \n').lower()

if choice == 'left':
    choice2=input('Okay! now you\'re in front of the sea! You can go swimming or wait the boat \n' 
                  'Type "swim" or "wait": \n').lower()
    if choice2 == 'wait':
        print(''' 
                             __/\__
                          ~~~\____/~~~~~~
                             ~  ~~~   ~.    
            ''')
        choice3= input( ' Now you\'re in a cave and there\'re three ways:\n' 
                       'Type the way you wanna follow:  "left", "middle" and "right": \n').lower() 
        if choice3 =='left':
        
             print("\nWow, Oh my God!!! You are amazing! \n"
                   "The treasure is yours!!!")  
        else:
            print("RIP: You choose wrong and badly you died!\n")
            print('''
                  
                          .-"""-.
                         | _   _ |
                         ](_' `_)[
                         `-. N ,-' 
                           |   |
                           `---'


                  
                  ''')   

    elif choice2=='swim':
        print(''''
                     .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'OO  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                       (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
        
        ''')
        print('\nRIP: You were swimming when a hungry and giant crocodile ate you!\n' 
              'The adventure is over!')
    else:       
        print("You didn't type a correct answer try again!")

elif choice == 'right':
    print(''''
          / \/
         /   \/
        /     \/
       /_______\/
       \/ . . \/
      (/(__7__)\)
      |'-' = `-'|
      |         |
      |\       /|
     |  '.   .'  |
    | /|  `"`  |\ |
    \ \|===LI==|/ /
     '-|_______|-'
        |__|__|
        |--|--|
       (__)`(__)
    ''')
    print("\nOh no! You found the gnome of bad luck and now you'll never find the treasure. The adventure is over ")
else: 
    print("You didn't type a correct answer try again!")