import time
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
            return f'{self.title} was an expensive movie: {True}'
        else:
            return f'{self.title} was an expensive movie: {False}'

#kuriami du Movie objektai: movie1 ir movie2        
movie1 = Movie('Blockbuster 9000', 'Mr. Fancy Pants', 900000000)
movie2 = Movie('TrashMovie', 'Mr. Trash van Bin', 5000)

#atspausdinam pažiūrėti ar viskas gerai su objektais
print('------ Movie 1: ------')
print(movie1)
time.sleep(2)
print('------ Movie 2: ------')
print(movie2)

time.sleep(4)
print('------ printing wasExpensive() method: ------')
time.sleep(2)

#atspausdinamas metodas wasExpensive pasakantis ar filmas buvo brangus. Grąžina True arba False
print('------ Movie 1: ------')
print(movie1.wasExpensive())
time.sleep(2)
print('------ Movie 2: ------')
print(movie2.wasExpensive())