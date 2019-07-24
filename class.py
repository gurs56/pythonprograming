"""
class Dog:
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

    def bark_hello(self):
        print(f"Woof Im called {self.name}. i am {self.age} human-years.")
#create dog object

spot = Dog()
print(spot.name)

dog_two = Dog("spot2", 3)
print(dog_two.name)
dog_two.bark_hello()
"""

#create an Inst account class
#the class has user_name,email,profile_pic,posts,followers

class InstagramAccount:
    def __init__(self, un, email):
        self.user_name = un
        self.email = email
        self.profile_pic = ""
        self.posts = []
        self.followers = []
    
    def make_post(self, post):
        self.posts.append(post)

    def following_me(self, another_account):
        self.followers.append(another_account)

    def get_posts(self):
        return self.posts

    def get_followers(self):
        return self.followers

    def __repr__(self):
        return "{username: " + self.user_name + " Email " + self.email + "}"

account_one = InstagramAccount("sahaj", "Gurs56@outlook.com")
#print(type(account_one))
account_two = InstagramAccount("bill", "bill@outlook.com")

account_one.make_post("first post")

print(account_one.get_posts())

account_one.following_me(account_two)
print(account_one.get_followers())