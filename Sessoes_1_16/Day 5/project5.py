import random

letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z' ]

symbols_list=['@',"#","$","%","&","*"]

numbers_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]



print('welcome')

letters=int(input("How many letters do you want in your password? \n"))

symbols=int(input("How many symbols do you like?\n"))

numbers=int(input("How many numbers do you like?\n"))

listy=[]


for letter in range(0, letters):
    listed=random.randint(0,letters)
    listy+=[letter_list[listed]]


#alternative model using choice and not randit
for symbol in range(0, symbols):
    symboled=random.choice(symbols_list)
    listy += [symboled]
    
    #OR
    # symboly += [random.choice(symbols_list)]
    # listy.append(random.choice(symbols_list))

for number in range(0,numbers):
    numbered = random.randint(0,numbers)
    listy+=[numbers_list[numbered]]
      

print(listy)
random.shuffle(listy)
resultado = " ".join(map(str, listy))
print(f"Suggestion of a strong password: {resultado}")


#alternative

# new_char=""

# for char in listy:
#     new_char+=str(char)

# print(new_char)


#create a for using the len of the code above
