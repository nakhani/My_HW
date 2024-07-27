from media import Media

class Film(Media):
    def __init__(self,name,director,IMDBscore, url, duration,casts,genre,date):
        super().__init__(name,director,IMDBscore, url, duration,casts)
        self.genre=genre
        self.createdate=date
        