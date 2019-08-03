burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "eggs", "beans", "spam"]

for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)