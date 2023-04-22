cars=['bmw','aubi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("Here is the original list:\n\t",cars)
print("\nHere is the sorted list:\n",sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)

print(len(cars))