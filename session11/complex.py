

class Complex():
    def __init__(self, real,image):
        self.real=real
        self.image=image

    def show(self):
        print(self.real,"+",self.image,"i")

    def sum(self, f1):
        new_real = self.real + f1.real
        new_image = self.image + f1.image
        result= Complex(new_real, new_image)
        return result
    
    def sub(self, f1):
        new_real = self.real - f1.real
        new_image = self.image - f1.image
        result= Complex(new_real, new_image)
        return result
    
    def mul(self, f1):
        new_real = (self.real * f1.real) - (self.image * f1.image)
        new_image = (self.image * f1.real) + (self.real * f1.image)
        result= Complex(new_real, new_image)
        return result

a = Complex(5,8)
a.show()

b = Complex(2, 3)
b.show()
# sum
c = a.sum(b)
c.show()
#sub
d = a.sub(b)
d.show()
#mul
e = a.mul(b)
e.show()