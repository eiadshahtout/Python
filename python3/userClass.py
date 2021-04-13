class User:
    
    def __init__(self, first_name, last_name, location, age, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.age = age
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is from {self.location} and is {self.age} years old ")
        
    def greet_user(self):
        print(f"Welcome to my place {self.first_name}!!! ")
        
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print(f"You have attempted {self.login_attempts} times to login")
        
    def reset_login_attempts(self, reset):
        if reset == 0 or reset == 'reset':
            self.login_attempts =0
            self.login_attempts = reset
            print("You reset the login attempts")
            
        
Users = User('James', 'Bond', 'London', '35', 0)

Users.increment_login_attempts(1)
Users.increment_login_attempts(4)
print(Users.login_attempts)
Users.reset_login_attempts(0)
print(Users.login_attempts)
Users.reset_login_attempts(0)
Users.increment_login_attempts(7)
Users.increment_login_attempts(7)
print(Users.login_attempts)
Users.reset_login_attempts(0)
print(Users.login_attempts)

