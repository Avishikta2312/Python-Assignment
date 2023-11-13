#Accept a string of comma separated words as input and generate a string of comma separated words (from the input string) sorted alphabetically.


li=[]
str=input("Enter a string:")
str=str.replace(","," ")
li=str.split()
n=len(li)
    
print("The elements that wanted to see in a sorted format:",li)
sorted_li=[]
sorted_li=sorted(li)                                           #sorted function is use to sort the list alphabatically
print("The sorted elements are:",sorted_li)

#Enter a string:mba, bca, btech, mca
#The elements that wanted to see in a sorted format: ['mba', 'bca', 'btech', 'mca']
#The sorted elements are: ['bca', 'btech', 'mba', 'mca']
