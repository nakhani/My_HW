class MyTime:

    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()
       

    def  show(self):
       print(self.hour,":",self.minute,":",self.second)

    def sum (self, other):
        new_s = self.second + other.second
        new_m = self.minute + other.minute
        new_h = self.hour + other.hour
        result = MyTime(new_s,new_m,new_h)
        return result
    
    def sub (self,other):
        new_s = self.second - other.second
        new_m = self.minute - other.minute
        new_h = self.hour - other.hour
        result = MyTime(new_s,new_m,new_h)
        return result
    
    def second_to_hour (self):
        while self.second >= 60:
           self.second -= 60
           self.minute += 1
           while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        result = MyTime(self.hour,self.minute,self.second)
        return result

    def hour_to_second (self):
        self.second = self.hour * 3600 + self.minute * 60 + self.second
        return self.second
    
    def fix(self):
      if self.second >= 60:
        self.second -= 60
        self.minute += 1

      if self.minute >= 60:
        self.minute-= 60
        self.hour += 1

      if self.minute < 0:
        self.minute += 60
        self.hour -= 1

      if self.second < 0:
        self.second += 60
        self.minute -= 1

    def gmt(self):
       teh_h = self.hour + 3
       teh_m = self.minute + 30
       teh_s = self.second 
       result = MyTime(teh_h,teh_m,teh_s)
       return result
    
    def plus(self):
       self.second +=1
       self.fix()

    def minus(self):
       self.second -=1
       self.fix()
