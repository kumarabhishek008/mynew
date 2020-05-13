from array import*
list = [1,3,4,5,6,7,8,9,11]
n=int(input("type a number"))

def search(list,n):
    for i in list:
        if i == n:
            return True


    return False

if search(list,n):
    print("found")
else:
    print("value not present in the list")


#sorting array and sort selection
arr = array('i',[])
n = int(input("enter a value"))

for i in range(n):
    x = int(input("value"))
    arr.append(x)

print(arr)
#sort array
def sort(arr):
    for i in range(n-1):

        pos = i
        for j in range(i,n):

            if arr[j]<arr[pos]:
                pos = j

        temp = arr[i]
        arr[i]=arr[pos]
        arr[pos] = temp
        print(arr)

sort(arr)

print(arr)

