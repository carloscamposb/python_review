from data import Menu, resources

profit=0

def is_resources_sufficients(ingredients):
    """Returns True when order can be made, and False if ingredients are insufficient"""
    is_enoght=True
    for item in ingredients:
       if ingredients[item] >= resources[item]:
        print(f'Sorry there is not enogh {item}')
        is_enoght= False
    return is_enoght 


def process_coins():
   """Returns the total calculated from coins inserted"""
   print("Please inset coins.")
   total=int(input('How many quarters? '))*0.25
   total+=int(input('How many dimes? '))*0.10
   total+=int(input('How many nickles? '))*0.05
   total+=int(input('How many pennies? '))*0.01
   return total 


def is_transaction_successful(money_received, drink_cost):
   '''Returns True when the payment is accepted, or False if money is insufficient '''
   if money_received > drink_cost:
      change = round(money_received - drink_cost,2)
      print(f"Here is ${change} in change.")
      global profit
      profit += drink_cost 
      return True
   else:
      print('Sorry there is not enoght money!')
      return False
    

def making_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {drink_name} coffee ☕')

machine_working = True
while machine_working:
    ask_coffee = input('What would you like? (espresso/latte/cappuccino): \n')
    #secret word to turn off
    if ask_coffee == 'off':
        machine_working=False
    #secret word to see the actual resources    
    elif ask_coffee == 'report':
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']} ml")       
        print(f"coffee:{resources['coffee']} ml" )
        print(f"Money: ${profit}")
    else:
       drink= Menu[ask_coffee]     
       if is_resources_sufficients(drink['ingredients']):
          payment=process_coins()
          is_transaction_successful(payment,drink['cost'])
          making_coffee(ask_coffee,drink['ingredients'])
