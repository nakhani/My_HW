from media import Media

class Clip(Media):
    def __init__(self,name,director,IMDBscore, url, duration,casts,date,topic):
        super().__init__(name,director,IMDBscore, url, duration,casts)
        self.createdate=date
        self.topic=topic