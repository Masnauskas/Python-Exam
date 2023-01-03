import time
# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]
print('Original users array:', users)
time.sleep(2)
print('---------------------------------------------------------------------------------------------------------------------')
# getUserAverageAge

def getUserAverageAge(array_input):
  #atsirenkam tik "age" ir sukuriam naują listą
  users_filtered = list(filter(lambda x: isinstance(x['age'], int), array_input))
  #skaiciuojam vidurkį
  #su sum() sudedam visus pasiimtus "age" value su get() ir padalinam iš masyvo ilgio len() - devyni
  #su round() suapvalinam skaičių
  return round(sum(i.get('age', 0) for i in users_filtered) / len(users_filtered))

print('User average age is:', getUserAverageAge(users))
time.sleep(2)
print('---------------------------------------------------------------------------------------------------------------------')

# getUsersNames

def getUsersNames(array_input):
  #kuriam naują masyvą users_names
  #naujam masyvui priskiariam visus name values interuodami per users(array_input) masyvą
  users_names = [x["name"] for x in array_input]
  #surikiuojam users_names masyvą abecelės tvarka
  users_names.sort()
  #gražinam surikiuotą masyvą
  return users_names
  
print('User names list sorted alphabetically:', getUsersNames(users))