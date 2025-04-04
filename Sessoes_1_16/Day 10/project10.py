from art import art

def add(number1,number2):
    return number1+number2

def sub(number1,number2):
    return number1-number2

def mult(number1,number2):
    return number1*number2

def div(number1,number2):
    if number2 == 0:
        return "error! Division by zero!"
    return number1/number2


dic_calculation={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div,
}


while True: 
    print(art)

    number1=float(input("Type the first number: \n"))

    while True:
        choice= input('Pick an operation:\n(+)\n(-)\n(*)\n(/): \n')

        if choice not in dic_calculation:
            print('Invalid operator')
            continue
        number2=float(input("Type the second number: \n"))         
        result= dic_calculation[choice](number1, number2)
        print(f' {number1}  {choice} {number2} = {result}')

        continue_calculation=input('Do you wanna do another calculation? (y) or (n): \n').lower()

        if continue_calculation=='n':
            print("Ok! Thank you")
            exit()     
        previous_input=input(f'Do you wanna use the previous result: {result}? (y) or (n) : \n').lower() 
       
        if previous_input=='y':
           number1=result
        else:
            print('\n'*20)
            break # Exit the inner loop
      
                   
        
       


 




# # my_calculation = dic_calculation['*']
# # print(my_calculation(4, 8)) 

# print(dic_calculation['*'](4,8))


