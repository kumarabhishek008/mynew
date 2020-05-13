
class person:
    def __init__(self,name,age,year):
        self.name = name
        self.age = age
        self.year = year

    def printperson(self):
        print(self.name,self.age,self.year)

x = person("abhishek","25",2019)
x.printperson()