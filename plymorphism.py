#duck typing

class pycharm:
    def execute(self):
        print("compiling")
        print("running")

class myeditor:
    def execute(self):
        print("chukels")
        print("debug")
        print("compiling")
        print("running")

class laptops:  ##it doesn't matter which object u r passing only matter is method should be same like execute here for ide.#

    def code(self,ide):
        ide.execute()

pych = myeditor()
lap1 = laptops()
lap1.code(pych)


#operator overloading
#> use methods for addition suntraction and multiplication not  pass operators for calculation in oops concept or method over loading
#method overloadin > when we pass two method with a same name in same class with diffrent prameters is called method overloading
# method overriding > iwhen we pass two methods with same name in diffrent class with same parameters is called method overriding
class A:
    def show(self):
        print("in show a")
class B(A):
    def show(self):
        print("im show B")


s1 = B()
s1.show() # this is method override because it is calling class B show() method not class A.


