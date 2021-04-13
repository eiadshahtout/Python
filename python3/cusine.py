class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
    
    def customer_numbers(self):
        print('This restaurant has {} customers right now'.format(self.number_served))
        
    def set_number_served(self, served):
        self.number_served = served
        
    def increment_number_served(self, customers):
        self. number_served += customers
        

restaurant = Restaurant('Chinese food', 'Hot Noodles')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.customer_numbers()
restaurant.set_number_served(15)
restaurant.customer_numbers()
restaurant.increment_number_served(5)
restaurant.customer_numbers()