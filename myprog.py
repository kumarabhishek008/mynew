from array import *
class person:
    def __init__(self,name,age,fathersname,mothersname,yourname):
        self.name=name
        self.age=age
        self.fathersname=fathersname
        self.mothersname=mothersname
        self.yourname=yourname

    def printbio(self):
        y = "abhishek kumar"
        if y == a :
         print(self.name)
        else:
            print("not amtched")
        z= 25
        if z==b:
         print(self.age)
        else:
            pass
        q="subodh pandit"
        if q==c:
         print(self.fathersname)
         print(self.mothersname)
         print(self.yourname)
        else:
            print("not matched")

a=input(" ")
b=int(input("age: "))
c=input("fathers name : ")
d=input("mothersname: ")
e=input("your name: ")

x=person(a,b,c,d,e)
x.printbio()
