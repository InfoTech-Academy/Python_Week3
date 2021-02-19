


def reading_number(number):
    dictionary1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7 :"seven", 8:"eiğht", 9:"nine"}
    dictionary2 = {11:"eleven",12:"twelve",13:"thirteen",14:"fourteen", 15:"fifteen", 16:"sixteen",
                   17:"seventeen", 18:"eiğhteen", 19:"nineteen"}
    dictionary3 = {1:"ten", 2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    
    number2=int(number)
    digit1=int(number[1])
    digit10=int(number[0])
   
    
    if number2<10:
        return (dictionary1.get(digit1))
        
    elif number2>10 and number2<20:
        return (dictionary2.get(number2))
        
    elif number2%10==0:
        return (dictionary3.get(digit10))
    
    else:
        return (dictionary3.get(digit10) + " " + dictionary1.get(digit1))
                   
print (reading_number(input("iki haneli bir sayı giriniz :")))