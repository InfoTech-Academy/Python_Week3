def unique(my_list):
    output1=[]
    
    my_list=list(my_list)
    for i in my_list:
        if i not in output1:
            output1.append(i)
    return output1
        
print(unique([1,2,3,4,3,3,5,9,8,7,5,7]))