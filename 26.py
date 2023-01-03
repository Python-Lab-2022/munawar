s=input("enter a string:")
length=len(s)
if length > 2:
    if s[-3:]=='ing':
        s=s+'ly'
        print(s)
    else:
        s=s+'ing'
        print(s)
