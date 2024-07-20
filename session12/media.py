from tabulate import tabulate
import pytube

class Media:
    def __init__(self,name,director,IMDBscore, url, duration,casts):
        self.name=name
        self.director=director
        self.IMDBscore=IMDBscore
        self.url=url
        self.duration=duration 
        self.casts=casts 

    def showinfo (self):
        data = [[self.name, self.director, self.IMDBscore, self.url, self.duration, self.casts]]
        print (tabulate(data))


    @staticmethod
    def download (f):
        link = f.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename=f.name + '.mp4')
