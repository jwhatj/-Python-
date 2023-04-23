pizza_calories=['bsk','kdj','beef']
for pizza in pizza_calories:
    print(pizza.title())
    print(f"{pizza.title()},I like pepperoni pizza!")
print("I really love pizza!")
pizza_calories.insert(-1,'linb')
print(pizza_calories)
friend_pizza=pizza_calories[:]
friend_pizza.append('love')
print("My favorite pizza are:")
for  pizza in pizza_calories:
    print(pizza.title())
print("My friend's favorite pizza are:")
for pizzas in friend_pizza:
    print(pizzas.title())