# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

#kuriama klasė Movie
class Movie:
    def __init__(self, title, director, budget):
        #klasei Movie priskiarimi title, director ir budget
        self.title = title
        self.director = director
        self.budget = budget
    
    # legvesniam ir patogesniam atvaizdavimui kuriama __str__ funkcija   
    def __str__(self):
        return f'Movie: {self.title}, director: {self.director}, budget: {self.budget} USD.'
    #kuriamas wasExpensive metodas, kuris pasakys ar filmas buvo brangus    
    def wasExpensive(self):
        if self.budget > 100000000:
            return f'Movie was expensive: {True}'
        else:
            return f'Movie was expensive: {False}'

#kuriami du Movie objektai: movie1 ir movie2        
movie1 = Movie('Blockbuster 9000', 'Mr. Fancy Pants', 900000000)
movie2 = Movie('Trash Movie', 'Mr. Trash van Bin', 5000)

#atspausdinam pažiūrėti ar viskas gerai su objektais
print(movie1)
print(movie2)

#atspausdinamas metodas wasExpensive pasakantis ar filmas buvo brangus. Grąžina True arba False
print(movie1.wasExpensive())
print(movie2.wasExpensive())