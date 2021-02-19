def equal_reverse(*my_str):
    global_result=[]
    x=0
    result=[] 
    for i in my_str:
                
        for j in i:
            if j==i[(len(i)-x-1)]:
                result.append(j)
                x+=1
        if list(i)==result:
            global_result.append(True)    
        else:
            global_result.append(False)
               
    return global_result 

print(equal_reverse("atam","madam" )) 