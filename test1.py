a = 33
b = "33"

if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

## The bug in this code i that b is string as it is written in quotation marks. We can't compare an int with a str. 
## If we remove the quotation marks from 33 the code works just as fine.