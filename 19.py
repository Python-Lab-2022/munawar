list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    list1.append(int(input()))
print(list1)
list1=list(filter(lambda x: x %2 !=0,list1))
print(list1)
