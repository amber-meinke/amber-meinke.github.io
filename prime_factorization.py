n = int(input("Please enter a number: "))
primeFactors = []

while n % 2 == 0:
    primeFactors.append(2)
    n = n/2
    
copy = int(n)
for i in range (3,copy+1,2):
    while n % i == 0:
        primeFactors.append(i)
        n = n/i
    
print(primeFactors)