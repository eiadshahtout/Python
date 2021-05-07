class Calculator:
    def add(self, x, y):
        self.x = x
        self.y = y
        result = self.x + self.y
        print(result)
    
    def subtract(self, x, y):
        self.x = x
        self.y = y
        result = self.x - self.y
        print(result)
    
    def multiply(self, x, y):
        self.x = x
        self.y = y
        result = self.x * self.y
        print(result)
    
    def divide(self, x, y):      
        self.x = x
        self.y = y
        if (y == 0):
            result = "You can't divide by zero!"
        else:
            result = self.x / self.y  
            print(result)
