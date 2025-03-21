#It's the same thing (subscribing)
print("Hello"[4])
print("Hello"[-1])

#Integer - whole number
print(23 + 65)

# Large Integers normally is represented by (,) though here in python is (_)
print(234_333_444)

#Float = Floating point number
print(3.1234)

# Boolean
print(True)
print(False)

#TypeError
# len(123)

#checking data type
print(type("Hello"))
print(type(123))
print(type(12.3))
print(type(False))

#Conversion
print(int("234"))

# TypeError: Can only concatenate str (not 'int') to str 
# print("Number of letters in your name: " + len(input("Enter your name")))

#Correction
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Mathematical operations in Python

#PEMDAS - parentheses, Exponents, Multiplication/Division, Adiction/Subtraction
# ()
# **
# * or /
# + or -

print(3*3+3/3-3) #Calculation is doing left to right
# 3*3
# 3/3
# 9+1-3
# 7
print(3*(3+3)/3-3)
# 3+3 =6
# 3*6= 18
# 18/3 =6
# 6-3=3

#round
print (round(3.3)) # 3
print (round(3.9)) # 4
# using a number of digits that you'd like in your result
print(round(3.97854, 2))

#f-String
score=29
winner=True
print(f"Your score is: {score} it means that are you winning? {winner}")

