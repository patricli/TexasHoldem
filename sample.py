

def isFizz(num):
    if(num % 3) == 0:
        return 1
    else:
        return 0

def isBuzz(num):
    if(num % 5) == 0:
        return 1
    else:
        return 0


def fizzbuzz(num):
    a = isFizz(num)
    b = isBuzz(num)
    if(a*b) == 1:
        return "FizzBuzz"
    elif(a):
        return "Fizz"
    elif(b):
        return "Buzz"
    else:
        return "Not divisable by 3 or 5"


#=========MAIN===============

def main():
    varInput = input("Enter number:")
    var = int(varInput)

    #print(fizzbuzz(var))

    while var:
        print(fizzbuzz(var))
        varInput = input("Enter number:")
        var = int(varInput)


if __name__ == "__main__": main()

