class Actor():

    #properties
    def __init__(self, name, surname, date, country):
        
        self.name = name
        self.surname = surname
        self.birth_date = date
        self.birth_country = country

    #methods
    def show(self):
        print("name & surname:", self.name,self.surname, "  born:", self.birth_date, "  birth country:", self.birth_country)

    def movie(self):
        f = open ("database.txt", "r")
        actor_movies=[]
        
        for line in f:
            result = line.split (",")
            
            movie = result[0]
            actors = result[5:len(result):1]
            
            if self.name in actors:
                actor_movies.append(movie)

        print(actor_movies)
        f.close()