# OOP works by using models to reduce complexity

# In a restaurant scenario, we have waiters, cooks, managers... each one being a model

# If we take the case of the waiter (my class), we have:
# waiter 1 and waiter 2- objects
# -> What they have (attributes):
# is_holding_plates = True 
# responsible_tables = [1, 2, 3]
# -> What they do (methods):
# def deliver_order(table, order): # delivers orders to the chef
# def take_payment(amount): # takes payment for the service

# =======USING LIBRARIES==========

#USING TURTLE
# from turtle import Turtle, Screen

# # Object and Class:
# timmy = Turtle() 

# timmy.shape("turtle") #object and method
# timmy.color('DarkGreen') #object and method
# timmy.forward(100)
# # Object and Class:
# my_screen = Screen()
# print(my_screen.canvheight) #object and atribute
# my_screen.exitonclick() # object and method

#USING PRETTYTABLE
# from prettytable import PrettyTable

# table=PrettyTable()
# print(table)


# # Mode 1 :

# # table.field_names=['Pokemon Name', 'Type']
# # table.add_row(['Pikashu', 'Electric'])
# # table.add_row(['Bulbasaur','Plant'])
# # table.add_row(['Squartle', 'Water'])
# # table.add_row(['Charizard', 'Fire'])

# # print(table)

# # Mode 2:
# table.add_column('Pokemon Name',['Pikashu', 'Bulbasaur', 'Squartle','Charizard'])
# table.add_divider()
# table.add_column('Type',['Electric','Grass/Poison', 'Water', 'Fire'])
# table.align='l' #using atribute
# print(table)

#USING RICH
from rich.console import Console
from rich.table import Table

console=Console()
table = Table()

table.add_column('Pokemon Name', justify='center' , style='yellow')
table.add_column('Type', justify='center', style='magenta')

table.add_row('Pikashu', 'Electric')
table.add_section()
table.add_row('Bulbasaur','Plant/Poison')
table.add_section()
table.add_row('Squartle', 'Water')
table.add_section()
table.add_row('Charizard', 'Fire')

console.print(table)