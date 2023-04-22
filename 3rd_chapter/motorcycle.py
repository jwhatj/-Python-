motorcycle=["honda",'yamaha','suzuki']
print(motorcycle)
motorcycle[0]="ducati"
print(motorcycle)
motorcycle.append("ducati")
print(motorcycle)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamada')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1,'saka')
print(motorcycles)
del motorcycles[2]
print(motorcycles)
popped_motorcycle=motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
first_owned=motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}")

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")