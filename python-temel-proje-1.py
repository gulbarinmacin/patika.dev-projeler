def make_flat(lst):
    flatten_list = []
    for i in lst:
        if not isinstance(i, list):
            flatten_list.append(i)
        else:
            flatten_list.extend(make_flat(i))
    return flatten_list
    
lst=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(make_flat(lst))
