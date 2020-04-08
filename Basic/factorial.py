# Factorial of user input

value = int(input())
fac = 1
for i in range(1, value+1):
    fac = fac * i
print(fac)

fac1 = 1
for i in range(value, 0, -1):
    fac1 = fac1 * i
print(fac1)