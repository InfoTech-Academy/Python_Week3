"""
A = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]
def tek(sayı):
    return sayı % 2 == 1

print(*filter(tek, A))"""
"""perfect_number.py
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000.
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions."""

def perfect_number(number):
    bölenler=[]
    
    for i in range(1,number):
        if number%i==0:
            bölenler.append(i)
    
    
    if sum(bölenler)==number:
        return number
    
    
fonksiyon_ciktisi=[]            
for i in range(1,1000):
    if (perfect_number(i)) != None:
        fonksiyon_ciktisi.append(perfect_number(i))
print(*filter(perfect_number,fonksiyon_ciktisi)) 
    


        