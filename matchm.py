#a=input('enter your name')
b=10
c=3
a=(input('enter number of seats you wish'))
match a:
    case '+' :
        amu=b+c
    case '_' :
        print('gold class')
        amu=b-c
    case '*' :
        print('silver class')
        amu=b*c
    case _:
        print('invalid class')
        amu=None
print(9)