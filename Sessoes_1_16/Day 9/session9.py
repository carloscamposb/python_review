# # To create an object

# my_object = {
#    "cat": "Animal which drinks milk",
#    "dog": "Animal which plays with balls",
# }

# # Calling the object

# print(my_object["cat"])

# # Creating an object from zero:
# # my_object = {}

# # Adding a new object
# my_object["bird"] = "They have feathers"
# print(my_object)

# # Changing the value:
# my_object["cat"] = "They like to hunt at night"
# print(my_object)

# # Using a loop:
# for key in my_object:
#     print(f'{key}:')
#     print(my_object[key])



# Nested list in dictionary

# travel_alog={
#     "Brasil": ['Pernambuco', 'São Paulo' , 'Belém do Pará'],
#     "USA": ['Ohio', 'Nevada' , 'New YorK'],
# }

# print(travel_alog['Brasil'][1])


nested_list= ["a", "b",["c", "d"]]  


print(nested_list[2][1])

#Dictionary nested in another dictionary

travel_log={
    "Brasil":{
        "states_viseted": ['Pernambuco', 'São Paulo' , 'Belém do Pará', 'Minas Gerais'],
        "total_viseted": 4
    },

    "EUA":{
        "states_viseted": ['Ohio', 'Nevada' , 'New YorK'],
        "total_viseted": 3
    }
   
}

print(travel_log["EUA"]["states_viseted"][2])


