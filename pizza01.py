prompt = "\nPlease enter the topping you want in your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "
toppings = []
while True:
    topping = input(prompt)
       
       
    if topping != 'quit':
        print(f"I have added {topping.title()} to your pizza!")
        toppings.append(topping)
        for a in toppings:
            print(a)
    else:
      break 
        



