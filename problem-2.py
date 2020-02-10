def isPrime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
                return False
       else:
            return True   
           
    else: 
        return False

def isFloatPrime(numFloat):
    for i in range(1,4):
        num = int(numFloat * (10**(i)) )
        if (isPrime(num)):
            return True
    return False

numFloat = float(input()) 
while (numFloat != 0.0):
    print(isFloatPrime(numFloat))
    numFloat = float(input()) 


