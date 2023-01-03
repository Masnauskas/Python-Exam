import time
# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

print('Original users array:', users)

time.sleep(2)
print('------------------------------------------------------------------------------------------------')

# filterDogOwers

def filterDogOwers(array_input): 
  return list(filter(lambda x: x["hasDog"] == True, array_input)) #programuojam lamba funkciją, kuri priima parametrą x. tada iš masyvo pasiimam "hasDog" ir filtruojam jeigu jo reikšmė True.
      
print('Has dogs: ',filterDogOwers(users))

time.sleep(2)

print('------------------------------------------------------------------------------------------------')

# filterAdults

def filterAdults(array_input):
  return list(filter(lambda x: x["age"] >= 18, array_input)) #programuojam lamba funkciją, kuri priima parametrą x. Tada iš masyvo pasiimam age ir filtruojam jeigu age daugiau ar lygu 18kai.

print('Only adults: ',filterAdults(users))