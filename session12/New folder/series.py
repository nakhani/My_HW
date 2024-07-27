from media import Media

class Series(Media):
    def __init__(self,name,director,IMDBscore, url, duration,casts,genre,season,episode):
        super().__init__(name,director,IMDBscore, url, duration,casts)
        self.genre=genre
        self.season=season
        self.episode=episode
        