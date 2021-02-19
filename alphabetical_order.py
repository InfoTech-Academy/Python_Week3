# alphabetical_order

def alphabetical(my_str):
    items=my_str.split("-")
    items.sort()
    my_str="-".join(items)
    return my_str
   
    
    
print(alphabetical(input("Write words separated with - : ")))
