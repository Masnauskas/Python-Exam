# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        
    def __str__(self):
        return f'Movie: {self.title}, director: {self.director}, budget: {self.budget} USD.'
        
    def wasExpensive(self):
        if self.budget > 100000000:
            return f'Movie was expensive: {True}'
        else:
            return f'Movie was expensive: {False}'
        
movie1 = Movie('Blockbuster 9000', 'Mr. Fancy Pants', 900000000)
movie2 = Movie('Trash Movie', 'Mr. Trash van Bin', 5000)

print(movie1)
print(movie2)

print(movie1.wasExpensive())
print(movie2.wasExpensive())