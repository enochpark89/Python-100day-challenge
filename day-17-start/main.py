# How do you create a class?
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # You don't have to receive parameter to create an attribute in a class
        self.followers = 0
        self.following = 0

    # Methods

    # Follower and following counts increase.
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Initialize the class?
user_1 = User("001", "Enoch")
user_2 = User("002", "Grace")

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)

"""
Output: 
1
1
"""