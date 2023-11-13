#Check if the items in a list are sorted in ascending order, or descending order, or not sorted.


li=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    li.append(ele)

if(all(li[i]<=li[i+1] for i in range(0,n-1))):            #by using all function here we chcek whether all the elements of the list are in the assending order
    print("The elements are in the assending order")
elif(all(li[i]>=li[i+1] for i in range(0,n-1))):          #by using all function here we chcek whether all the elements of the list are in the desending order
    print("The elements are in the desending order")
else:
    print("The elements are not in the sorted order")
    
#Enter the number of elements:4
#Enter the element:2
#Enter the element:4
#Enter the element:6
#Enter the element:8
#The elements are in the assending order
