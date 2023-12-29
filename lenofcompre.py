a=['abcd',{1:2,3:1,1:3},[4,5,6],{4,7},(9,8,7)]
b=[i for i in a if len(i)>2]
print(b)
