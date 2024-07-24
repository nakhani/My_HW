class Actor():

    #properties
    def __init__(self, name, surname, date, country):
        
        self.name = name
        self.surname = surname
        self.birth_date = date
        self.birth_country = country

    #methods
    def show(self):
        print("name & surname:", self.name,self.surname, "  born:", self.birth_date, "  birth country:", self.birth_country)
    
    
    @staticmethod
    def actor():
     CAST = []
     while True:
        Q = input("Do you want to add any cast? (y/n)")
        if Q == "y":       
            cast = input("enter cast: ")
            CAST.append(cast)
        elif Q == "n":
            return CAST
        else :
           print("Please  enter y/n")