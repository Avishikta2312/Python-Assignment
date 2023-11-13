#Break a list into chunks of size N.


li=[1,2,3,4,5,6,7,8,9,10]
n=len(li)
chunks=int(input("Enter the size of chunks:"))
for i in range(0,n,chunks):                     #by using for loop we interate the list of elements
    x=i
    print(li[x:x+chunks])                       #by using slicing method we slice the list with size N
    
    
    
    
#Enter the size of chunks:4
#[1, 2, 3, 4]
#[5, 6, 7, 8]
#[9, 10]
