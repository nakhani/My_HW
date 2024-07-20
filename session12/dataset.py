from media import Media

class Dataset(Media):

    #properties
    def __init__(self, n):
        
        self.name = n

    #methods
    def read(self):

        f = open (self.name, "r")
        
        for line in f:
            result = line.split (",")
            result[len(result)-1] = result[len(result)-1].strip()
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5:len(result):1])
            MOVIES.append(my_obj)
            MOVIE_NAMES.append(result[0])
            ACTORS.append(result[5:len(result):1])
        
        f.close ()
       
    def write(self):
        
        f = open(self.address, "w")
        
        for movie in MOVIES:
            delimiter = ','
            my_string = delimiter.join(movie.cast)

            f.write(movie.name + ",")
            f.write(movie.director + ",")
            f.write(movie.score + ",")
            f.write(movie.url + ",")
            f.write(movie.duration + ",")
            f.write(my_string+'\n')

        f.close ()