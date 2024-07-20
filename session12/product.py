import pyfiglet 
from termcolor import colored
from media import Media

class Product():
     def __init__(self,name,director,IMDBscore, url, duration,casts):
         super().__init__(name,director,IMDBscore, url, duration,casts)



     @staticmethod
     def add():
           CAST = []
           print(colored("_____________________________________________________\n",color="light_grey"))
           name= input("Enter movie's name:")
           director = input("Enter movie's director:")
           IMDBscore = input("Enter movies's IMDB score:")
           url = input("Enter download url:")
           duration = input("enter movie duration (first put an space and enter with this format: 02h06m): ")
           while True:
            Q = input("Do you want to add any cast? (y/n)")
            if Q == "y":
                cast = input("enter cast: ")
                CAST.append(cast)
            else:
                break

           new_movie = Media(name, director, IMDBscore, url, duration, CAST)
           return new_movie
     
     @staticmethod
     def edit():
          ...
     @staticmethod
     def remove():
          ...
     @staticmethod
     def search():
          ...
     @staticmethod
     def showlist():
          ...