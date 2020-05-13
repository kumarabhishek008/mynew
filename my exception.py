from myprog import*
class A:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature1")

class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature2(self):
        print("feature 2")

class C(B,A):
    def feature3(self):
        print("feature3")

x= person(a,b,c,d,e)
a=C()
a.feature2()