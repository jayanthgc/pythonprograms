#print cube of a number divisible by 3 fromm range 1-25
a=(i**3 for i in range(1,25) if i%3==0)
print(a)