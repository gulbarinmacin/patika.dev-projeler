# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:48:57 2021

@author: gulbarin
"""

def insertion_sort(mylist):
	for i in range (1, len(mylist)):
		j = mylist[i]
		while mylist[i-1] > j and i > 0:
			mylist[i], mylist [i-1]=mylist[i-1], mylist[i]
			print(mylist)
			i= i-1
            
print("\n first list  ")
insertion_sort([22,27,16,2,18,6])
print("\n second list ")
insertion_sort([7,3,5,8,2,9,4,15,6])