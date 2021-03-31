responses = {}

polling_responses = True

while polling_responses:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    
    if repeat == "no":
        break

print("\n--- Poll Results ---")
print(responses)
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")