class computer:
    school = "abhi university"
    processor = "i5"
    def __init__(self):
        self.name ="asus"
        self.ram = 8

    def compare(self,other):
        if (self.ram == other.ram):
            print("they are same")
        else:
            print("they are not same")
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is student class in abc method")

    class A :
        def feature1(self):
            print("feature 1")
        def feature2(self):
            print("feature2")
    class B(A):
        def feature1(self):
            print("feature 1")
    class c(B,A):
        def feature1(self):
            print("abhishek")




c1 = computer()
print(c1.getschool())
c1.info()
c2 = computer()
c2.ram = 8
c1.compare(c2)
print(c1.name,c1.ram,c1.processor)
print(c2.name,c2.ram)
a= computer.B()
print(a.feature2())