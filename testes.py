
# ======= COUNT PARTS IN A STRING

# string = input("Say something: ").lower()
# sub_string = input("Say another thing: ").lower()

# count = 0
# for i in range(len(string) - len(sub_string) + 1): 
#     if string[i:i + len(sub_string)] == sub_string:  
#         count += 1  

# print(f"The substring appears {count} times.")



# ======== COUNT LETTERS

# string = input("Say something: ").lower()
# letter = input("Say another thing (single letter): ").lower()

# count = string.count(letter)  # Conta quantas vezes a letra aparece

# print(f"The letter '{letter}' appears {count} times.")

# ======== ZIP FUNCTION 
# list_1=[100,200,300,400]
# list_2=['Carlos', 'Felipe', 'Marcela' , 'Marta']

# print(dict(zip(list_2,list_1)))


# ======= USING TIME
# import time
# for i in range (5,0,-1):
#     print(i, end='\r')
#     time.sleep(1)
# print('finished')    