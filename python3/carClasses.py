class Car:
    def __init__(self,make,model,year):
        self.mk = make
        self.model = model
        self.year = year
    def description(self):
        description_car = print(f"{self.mk} {self.model} {self.year}")
        return description_car.title()

my_new_car = Car("Audi", "a4", 2019)
print(my_new_car.description())