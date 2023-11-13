#The str.count() counts the number of non-overlapping occurrences of a specified substring in a string. E.g., if myStr = ‘Banana’, myStr.count(‘an’) returns 2, but myStr.count(‘ana’) returns 1. Write a Python script that includes the overlapping cases also.


def count_function(str,substring): #return the number of occurance of ovalaping substring
    count=0
    start=0
    while(len(str)>start):          #check whether length of the string is lesser than the value of strart position
        pos=str.find(substring,start)   #check whether the substring is present in the given string and here the search is start from the position start variable
        if(pos!=-1):                    #if the substring present in the given string then it return the first occurence position of the substring otherwise it will return -1
            start=pos+1                 #if the substring is found in the string then assing  the first occurence position in the start value
            count=count+1               #increase the count value by 1
        else:
            break
    return count
str="banana"
print("Number of occurance of the overlaping substring:",count_function(str,"an"))

#Number of occurance of the overlaping substring: 2
