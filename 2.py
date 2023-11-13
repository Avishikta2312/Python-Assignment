#Find all duplicate characters in a string.



str=input("Enter any string:")
l=list(str)                   #list() function is use to convert a string into list
unique_list1=[]
duplicate_list2=[]
for i in l:
    if i not in unique_list1 :
        unique_list1.append(i)
    elif i  not in duplicate_list2:
        duplicate_list2.append(i)
print("the unique elements are:",unique_list1)
print("The duplicate elements are:",duplicate_list2)

#Enter any string:AvishiktaDas
#the unique elements are: ['A', 'v', 'i', 's', 'h', 'k', 't', 'a', 'D']
#The duplicate elements are: ['i', 'a', 's']