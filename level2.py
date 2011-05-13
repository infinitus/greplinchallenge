#!/usr/bin/env python
import math

minNumber = 227000 
fiboNew = 1
fiboOld = 0 
fiboPrime = False
primeFactor = 2
sumOfPrimeFactors = 0

def isPrime(number):  
    if number <= 1:  
        return False  
    divisor = 2
    divisorMax = (int(math.sqrt(number)+1))
    while divisor < divisorMax:  
        if number % divisor == 0:  
            return False  
        divisor += 1  
    return True

while True:
    fiboNum = fiboOld
    if fiboNum > minNumber:
        if isPrime(fiboNum) == True:
            break;
    fiboNum = fiboNew
    fiboNew += fiboOld
    fiboOld = fiboNum

fiboNum += 1
print fiboNum

while fiboNum != 1:
    if isPrime(primeFactor) == True:
        while fiboNum % primeFactor == 0:
            fiboNum = fiboNum / primeFactor
            sumOfPrimeFactors += primeFactor
            print ("/" + str(primeFactor) + "=" + str(fiboNum))
    primeFactor += 1

print("Sum of prime factors = " + str(sumOfPrimeFactors))
