def make_sandwhich(*toppings):
    """Summarize the sandwhich we are about to make."""
    print("\nMaking a sandwhich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_sandwhich('pepperoni')
make_sandwhich('mushrooms', 'green peppers', 'extra cheese')