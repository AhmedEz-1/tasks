def is_prime() :
    x = int(input("Enter a number:"))
    if x <= 1 :
        print(x , "is not a prime number")
    for y in range(2 , x):
        if x % y == 0:
            print(x ,"is not a prime number")
            return        
    print(x , "is prime number")
is_prime()


