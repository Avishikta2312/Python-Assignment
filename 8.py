#Find N largest elements from a list.


li=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):                           #enter the elements into a list
    ele=int(input("Enter the element:"))
    li.append(ele)
    
print("The elements are:",li)

num=int(input("Enter the number of largest elements:"))       #Enter the number of the largest elements

li=sorted(li,reverse=True)                    #sorted the elements in the desending order
print("ther N largest numbers are:",li[:num]) #print the N number of largest number using slicing method

#Enter the number of elements:8
#Enter the element:44
#Enter the element:48
#Enter the element:34
#Enter the element:24
#Enter the element:8
#Enter the element:18
#Enter the element:14
#Enter the element:2
#The elements are: [44, 48, 34, 24, 8, 18, 14, 2]
#Enter the number of largest elements:4
#ther N largest numbers are: [48, 44, 34, 24]

