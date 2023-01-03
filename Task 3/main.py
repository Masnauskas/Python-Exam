# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# showObjectKeys
# Kuriama showObjectKeys funkcija, bet ji rodys values, ne keys. Funkcijos pavadinimas iš užduoties.
def showObjectKeys(user_input):
  # su list() gaunam list'ą ir values() į tą list'ą įdedam audi dictionary "values"
  return list(user_input.values())

print('Audi list values:',showObjectKeys(audi))