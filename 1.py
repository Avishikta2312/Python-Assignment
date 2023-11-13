#Check if a string is palindrome or not.

str=input("Enter any string:")
str=str.replace(" ","") #replace function is use to remove all the white space in the string
rev_str=str[::-1]
if(str==rev_str):
    print("The string is palindrom")
else:
    print("The string is not a plaindrome")
    
#Set1
#Enter any string:Was it a car or a cat I saw
#The string is not a plaindrome

#Set2
#Enter any string:Students of MCA
#The string is not a plaindrome