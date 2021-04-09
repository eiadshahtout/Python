class User:
    def __init__(self,fn,ln,age,followers):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.followers = followers
    def describe_user(self):
        print(f"{self.fn} {self.ln} is {self.age} and has {self.followers} followers")
    def greet_user(self):
        print(f"Welcome {self.fn} {self.ln} :) ")

joe = User("Joe", "Doe", 23, 89)
micheal = User("Micheal", "Reeves", 32, 5000)
print("-" * 140)
joe.describe_user()
joe.greet_user()
print("-" * 140)
micheal.describe_user()
micheal.greet_user()
print("-" * 140)
