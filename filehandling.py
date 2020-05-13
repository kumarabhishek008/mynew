
f=open('a.py','r')
j = [1,2,3,4,5]
for i in f:
    print(i)

j.insert(-1,i)
print(j)