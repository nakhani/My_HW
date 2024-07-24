
from termcolor import colored
from tabulate import tabulate
from dataset import MOVIES
from dataset import MOVIE_NAMES
from tabulate import tabulate
from actor import Actor
from media import Media
from pytube import YouTube

class Product(Media):
    def __init__(self,name,director,IMDBscore, url, duration,casts):
        super().__init__(name,director,IMDBscore, url, duration,casts)

    
    @staticmethod
    def add():
           print(colored("_____________________________________________________\n",color="light_grey"))
           name= input("Enter movie's name:")
           director = input("Enter movie's director:")
           IMDBscore = input("Enter movies's IMDB score:")
           url = input("Enter download url:")
           duration = input("enter movie duration (first put an space and enter with this format: 02h06m): ")
           result = Actor.actor()

           new_movie = Media(name, director, IMDBscore, url, duration, result)
           MOVIES.append(new_movie)
           print(colored("New movie was added successfully", color="light_green"), "✔")

     
    @staticmethod
    def remove():
      print(colored("_____________________________________________________\n",color="light_grey"))
      name = input("Enter movie's name:")

      for movie in MOVIES:
       if movie.name== name:
         MOVIES.remove(movie)
         print(colored("Delete Done", color="light_green"), "✔")
         break
      else:
         print(colored("Not Found\n",color="light_red"))


    @staticmethod
    def edit():
        name = input(colored("enter the new name: ", color="green"))
    
        if name in MOVIE_NAMES:
            for movie in MOVIES:
                
                if movie.name == name:
                   movie.showinfo()
                   Product.sub_edit()
                   choice = int(input(colored("Enter your choice:", color="light_magenta")))
                   while True:
                      if choice == 1:
                         movie.name = input("enter the new name: ")
                         print(colored("Edit Done successfully", color="light_green"),"✔")
                         break
                      elif choice == 2:
                         movie.director = input("enter the new director: ")
                         print(colored("Edit Done successfully", color="light_green"),"✔")
                         break
                      elif choice == 3:
                         movie.score = input("enter the new score: ")
                         print(colored("Edit Done successfully", color="light_green"),"✔")
                         break
                      elif choice == 4:
                         movie.url = input("enter the new url: ")
                         print(colored("Edit Done successfully", color="light_green"),"✔")
                         break
                      elif choice == 5:
                         movie.duration = input("enter the new duration: ")
                         print(colored("Edit Done successfully", color="light_green"),"✔")
                         break
                      elif choice == 6:
                        result = Actor.actor()
                        movie.cast = result
                        print(colored("Edit Done successfully", color="light_green"),"✔")
                        break
                      elif choice == 7:
                        break
                      else:
                        print ('Select from 1 to 7!')
                        choice = int(input(colored("Enter your choice:", color="light_magenta")))
    
    @staticmethod         
    def sub_edit():
        
        print("1_name")
        print("2_director")
        print("3_score")
        print("4_url")
        print("5_duration")
        print("6_cast")
        print("7_EXIT")
        
       
    @staticmethod
    def search():
        search = int(input(" 1_search by name \n 2_search by Running time \n "))

        if search == 1:

            user_input = input ('enter movie name or movie director: ')
            for movie in MOVIES:
                if movie.name == user_input or movie.director == user_input:
                    movie.showinfo()

        elif search == 2:
                
            print("enter the desired range of movie running time in minute (X to Y minutes): ")
            X = int(input("X: "))
            Y = int(input("Y: "))
                
            for movie in MOVIES:
                hour = int(movie.duration[1:3])
                min = int(movie.duration[4:6])
                total = hour*60 + min
                if X <= total <= Y:
                    movie.showinfo()
                    
        else:
            print("select 1 or 2")
            Product.search(MOVIES)
              

    @staticmethod
    def showlist():
        col_names = ["name", "    director", "    score", "      URL", "                           duration", "cast"]
        print(tabulate("",headers= col_names))
        for movie in MOVIES:
            obj= Media.showinfo(movie)

    @staticmethod
    def download ():
        user_input = input ('enter movie name or movie director: ')
        for movie in MOVIES:
         if movie.name == user_input or movie.director == user_input:
           link = movie.url
           YouTube(link).streams.first().download(output_path='./', filename=link.name + '.mp4')
           