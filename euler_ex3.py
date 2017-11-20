#Euler project #3 - print the largest prime factor of a number var

def prime_factor(foo):
    div = 2;
    while foo % div:
        div = div + 1
    return div



def main():
    print("Hello world")
    var = 200
    largest_prime = prime_factor(var)
    print(largest_prime)
    while largest_prime > 1:
        var = var/largest_prime
        largest_prime = prime_factor(var)
    print(largest_prime)



    #print(prime_factor(var))


if __name__ == "__main__":
    main()