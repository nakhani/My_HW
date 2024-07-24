from media import Media


MOVIE_NAMES = []
MOVIES = []
ACTORS = []

class Dataset(Media):

    #properties
    def __init__(self,n):
        self.namee= n 
        

    #methods
    def read(self):

        f = open ("database.txt", "r")
        
        for line in f:
            result = line.split (",")
            result[len(result)-1] = result[len(result)-1].strip()
            obj = Media(result[0], result[1], result[2], result[3], result[4], result[5:len(result):1])
            MOVIES.append(obj)
            MOVIE_NAMES.append(result[0])
            ACTORS.append(result[5:len(result):1])
        
        f.close ()
       
    def write(self):
        
        f = open("database.txt", "w")
        
        for movie in MOVIES:
            split = ','
            my_string = split.join(movie.casts)

            f.write(movie.name + ",")
            f.write(movie.director + ",")
            f.write(movie.IMDBscore + ",")
            f.write(movie.url + ",")
            f.write(movie.duration + ",")
            f.write(my_string+'\n')

        f.close ()