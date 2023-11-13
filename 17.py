#Pair up consecutive elements of a given list.


li=[1,3,2,5,4]
n=len(li)
new_list=[]
for i in range(0,n-1):            #by using for loop we pair up the consecutive elements of the list
    res=[li[i],li[i+1]]
    new_list.append(res)
print(new_list)



#[[1, 3], [3, 2], [2, 5], [5, 4]]
