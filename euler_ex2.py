n1 = 1
n2 = 1
total = 0  # sum of even numbers

while n2 < 4000000:  #while last fib less than 4 million
    n3 = n1 + n2
    print(n3)
    if(n3%2 ==0):
        total = total + n3
    n1 = n2
    n2 = n3

print("total")
print(total)  #print answer