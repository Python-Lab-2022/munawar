str=input("enter the list of words(Space seperated):")
list=str.split()
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len(i)
        temp=i
print("longest word in the list is :",temp)
print("length of ",temp,"is",len(temp))
