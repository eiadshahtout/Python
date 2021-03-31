responses = {}

polling_responses = True

while polling_responses:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no)? ")
    
    if repeat == "no":
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to go to {response}.")