#Find words in a string which are greater than some given length k.

str=input("Enter any string:")
num=int(input("Enter any length:"))
str=str.replace(","," ")
list1=str.split()
for i in list1:
    if(len(i)>num):          #check the words whose length are grater than the giver number
        print(i)
        
#Enter any string:If debugging is the process of removing bugs, then programming must be the process of putting them in.
#Enter any length:7
#debugging
#removing
#programming