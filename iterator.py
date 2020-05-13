# iterator

class person:
    def __init__(self):
        self.nums = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums<=10:
            val = self.nums
            self.nums +=1

            return val
        else:
            raise StopIteration
valves = person()
print(next(valves))


for i in valves:
    print(i)


# generators > where we use yield to generate values


class A:

    def my(self):
        n=1
        while n<=10:
            nq = n*n

            yield nq
            n += 1
            

a = A()
c=a.my()

for i in c:
    print(i)

#iteration

a=(1,2,3,4,5,6,7,8,9)
b=iter(a)
print(b.next())
print(b.next())
print(b.next())