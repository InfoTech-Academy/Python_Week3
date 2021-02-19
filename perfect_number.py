
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
    


        