def describe_pet(animal_type, pet_name = "dog"): 
    """Display information about a pet."""
    print(f"You have a {animal_type}.")
    print(f"The {animal_type}'s name is {pet_name.title()}.")

animaltype = input("What's the animals type? ")
animalName = input(f"What is the {animaltype}'s name? ")

describe_pet(animaltype, animalName)
