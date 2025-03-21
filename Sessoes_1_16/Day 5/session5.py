# for loops

materials=['book', 'table' , 'pencil']

for material in materials:
    print(f'I have a {material}')

print(materials)




#Creating a function equal to sum()
score_number=[1,44,242,66,90,422,57,32,789,222,79,1,5,8,90,0,67,545,232,35,7,898,9,0,321,3,5,7,8,9,80,9,90,8,56,4,532,4,21]

total= sum(score_number)

print(total)

count=0

for score in score_number:
    count+=score

print(count)    

# Creating a function equal to max()

print(max(score_number))

max_value=0
for n in score_number:
    if n > max_value:
        max_value=n
 
print(max_value)        


# Creating a function equal to max()


print(min(score_number))

min_value=999
for n in score_number:
    if n < min_value:
        min_value=n
   
print(min_value)        


sum=0
for number in range(1,101):
    sum+=number
print(sum)   