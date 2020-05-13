class file_option:
    def newfile(self):
        file = open('a.py','r')
        for i in file:
            print(i)



r = file_option()
r.newfile()
