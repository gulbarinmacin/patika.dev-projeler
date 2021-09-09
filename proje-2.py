def reversing(lst):
    new_list=[]
    for elem in lst:
        elem=elem[::-1]
        new_list.append(elem)
    
    return new_list[::-1]
    
lst=[[1, 2], [3, 4], [5, 6, 7]]
print(reversing(lst))