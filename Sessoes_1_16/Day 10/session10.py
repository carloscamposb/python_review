# # function with Output
# names=''
# def full_name(first_name, last_name):
#   return first_name + " " + last_name


# f_name=input('write your first name: ').capitalize() #capitalises just the first word of the entire string. title() is used for every word of a setence
# l_name=input('write your last name here: ').capitalize()


# print(full_name(f_name, l_name))

def function_1(text):
   #doctring
   '''
        This is a function witch will repeat the text like a eco 
   '''
   return text + text

def function_2(text):
    return text.title()
    

print(function_2(function_1('hello')))

help(function_1)
