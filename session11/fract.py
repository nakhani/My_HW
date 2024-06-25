from math import gcd

class Fraction:
    #properties
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    #methods
    def dev (self, f1):
        result_s = self.num1 * f1.num2
        result_m = self.num2 * f1.num1
        x = Fraction(result_s, result_m) 
        return x 
    def sub (self,f1):
        result_s = self.num1*f1.num2 - f1.num1*self.num2
        result_m = self.num2* f1.num2
        x = Fraction(result_s, result_m) 
        return x 
    def sum (self, f1):
        result_s = self.num1*f1.num2 + f1.num1*self.num2
        result_m = self.num2* f1.num2
        x = Fraction(result_s, result_m) 
        return x 
    def conv (self):
        result_s = self.num1/self.num2
        # x = Fraction(result_s)
        print(result_s) 
    def mult (self, f1):
        result_s = self.num1 * f1.num1
        result_m = self.num2 * f1.num2
        x = Fraction(result_s, result_m) 
        return x 
    def reduction (self):
        b = gcd(self.num1,self.num2)
        x = self.num1 // b
        y = self.num2 // b
        x = Fraction(x,y)
        return x
    def show (self):
        print(self.num1, "/" , self.num2)

a = Fraction (8,9)
b = Fraction (10,10)

b.show()
a.show()

# #sum
sumz = a.sum (b)
sumz.show()

# #sub
subz = a.sub (b)
subz.show()

# #dev
devz = a.dev(b)
devz.show()

# #mult
multz = a.mult(b)
multz.show()

# #conv
convz = a.conv()

# #reduction
reducz = a.reduction()
reducz.show()

