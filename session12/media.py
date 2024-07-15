class Media:
    def __init__(self,name,director,IMDBscore, url, duration,casts):
        self.name=name
        self.director=director
        self.IMDBscore=IMDBscore
        self.url=url
        self.duration=duration 
        self.casts=casts 

    def showinfo (self):
        ... 

    def download (self):
        ...