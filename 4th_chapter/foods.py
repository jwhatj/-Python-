my_food=['pizza','falafel','carrot cake']
friends_food=my_food[:]
my_food.append('cannoli')
friends_food.append('ice cream')
print("My favorite foods are:")
print(my_food)
print("\n\tMy friend's favorite foods are:")
print(friends_food)
for dogs_food in my_food:
    print(dogs_food.upper())