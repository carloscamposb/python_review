#Creating our own Class

class User:
    # Constructor
    def __init__(self, user_id, username): #using to inicialize atributes
        self.id = user_id
        self.username=username
        self.follower=0 #when its 0 you dont need to pass as a parameter
        self.following=0
    
    #Creating Methods
    def follow(self,user):
        user.follower +=1 #  It's the one being followed
        self.following +=1 # user who is doing the following
    
    
user_1 = User('001','Carlos') #object

# print(user_1.follow)

user_2 = User('002','Fabian') 

# user_1.id='001' #atribute is a variable associate with the object
# user_1.username='Carlos' #atribute 
# user_1.cpf='000.000.000-00' #atribute

#Carlos follows Fabian
user_1.follow(user_2)

print(user_1.follower) # output:0 (no one followed Carlos)
print(user_1.following)# output:1 (Carlos is following Fabian)
print(user_2.follower) # output:1 (Fabian got 1 follow from Carlos)
print(user_2.following)# output:0 (Fabian is not following anyone)


