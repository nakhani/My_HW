from media import Media

class Documentary(Media):
    def __init__(self,name,director,IMDBscore, url, duration,casts,date):
        super().__init__(name,director,IMDBscore, url, duration,casts)
        self.createdate=date
        