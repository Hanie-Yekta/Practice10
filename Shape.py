import math

class Shape:
    def __init__(self,P,S):
        self.p=P
        self.s=S
    
    def show(self):
        print("P: ",self.p)
        print("S: ",self.s)

class Circle(Shape):
    def __init__(self,R):
        super().__init__(P=self.p,S=self.s)

        self.r=R

    #tabe mohasebeye mohit dayere
    def p(self):
        self.p=(self.r*2)*math.pi

    #tabe mohasebeye masahat dayere
    def s(self):
        self.s=(math.pow(self.r,2))*math.pi
    

class Rectangle(Shape):
    def __init__(self,W,L):
        super().__init__(P=self.p,S=self.s)

        self.w=W
        self.l=L

    #tabe mohasebeye mohit mostatil
    def p(self):
        self.p=(self.l+self.w)*2

    #tabe mohasebeye masahat mostatil
    def s(self):
        self.s=self.w*self.l


################################################

print("Enter one of these options:\n1.Circle\n2.Rectangle")
choice=int(input("-->"))

if choice==1:
    #vared kardn meqdar shoa tavasot karbar
    c1=int(input("Enter the value of radius:"))

    #sakht obj az class circle
    obj_c=Circle(c1)
    
    obj_c.p()
    obj_c.s()
    obj_c.show()


elif choice==2:
    #vared kardn meqdar tul va arz tavasot karbar
    w1=int(input("Enter the value of width:"))
    l1=int(input("Enter the value of length:"))

    #sakht obj az class rectangle
    obj_r=Rectangle(w1,l1)

    obj_r.p()
    obj_r.s()
    obj_r.show()
    