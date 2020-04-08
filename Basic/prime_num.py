# Prime number = number divisible by itself and 1
# check if number is prime number

var = int(input())
if var > 1:
    for i in range(2, var):
        if var % i == 0:   # find factorials
            print(var, " is not a Prime number")
            break
    else:
        print(var, " is a Prime number")
