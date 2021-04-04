def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"The size of the pizza will be {size}")
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")



