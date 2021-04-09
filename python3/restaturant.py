class Resturant:
    def __init__(self,name,openorclosed,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.openorclosed = openorclosed
    def describe_resturant(self):
        print(f"{self.name} has {self.cuisine}")
    def open_resusturant(self):
        print(f"{self.name} is {self.openorclosed}")

Mcdonalds = Resturant("Mcdonalds", "Open", "Chips")

print(f"{Mcdonalds.name} is {Mcdonalds.openorclosed} and serves {Mcdonalds.cuisine}")
Mcdonalds.describe_resturant()