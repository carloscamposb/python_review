#Random Module

import random
# import my_module #module


# print(my_module.my_favorite_number)

random_integer= random.randint(10,14) #This randit is the function that someboby created in a model 
print(random_integer)

#when you arent really sure about the range (0 to 1)
random_float= random.random() # Nothing goes inside
print(random_float)

random_float2=random.uniform(1,10)                                                                                                
print(random_float2)



coin=random.randint(1,2)

if coin ==1:
    print('Heads')
else:
    print('Tails')



 #Lists

fruits=['Apple', 'Banana' , 'Grape']
print(fruits[1])
#-1 -2 ... it starts count from the end of the list
fruits[1]='Watermelon'
print(fruits)

#add some stuff in the list
fruits.append('Banana')
#append will coding a single iten in the end of the list
print(fruits)

#to add more than one iten
fruits.extend(['Passion Fruit', 'Melon'])
print(fruits)

# Creating a list with two different groups
fruits= ['Apple', 'Banana' , 'Grape']
vegetables= ['Onion', 'Tomate' , 'Garlic']

food=[fruits,vegetables]

print(food)


