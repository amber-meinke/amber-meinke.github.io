def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        
        for x in range (2,num):
            if num % x == 0:
                return False
        return True

n = int(input("Please enter a number: "))
primes = []

for i in range (1,n+1):
    if isPrime(i):
        primes.append(i)
        
print(primes)        