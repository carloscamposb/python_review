# def great():
#     print('hello')
#     print('Hi')
#     print('Hey')


# great()    

# # Function that allows parameters

# def great_someone(name):
#     print(f'hello {name}')
#     print('Hi')
#     print('Hey')

# great_someone('Carlos')

#name is the parameter and Carlos is my argument. 

#Challenge: How many weeks we left based on your age. 90 is the age!
# def weeks_left(age):
#     years_left= 90 - age
#     week= 52 * years_left
#     print(f"You've already {week} weeks left") 

# weeks_left(32)

## Using 2 parameters in a function:
def two_things(name,location):
    print(f"Hello {name}")
    print(f"Where've you been coming to visit us in {location}")

two_things('Carlos', 'Pune')  
two_things(name='Carlos', location='Pune')  
two_things(location='Pune',name='Carlos')  
# using position arguments doesnt care the position of the argument
