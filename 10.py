#Sum the digits of individual elements in a list of numbers.


def sum_of_digit(num):   #a function which is use to calculate the sum of digits of a number
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum

li=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):                           #enter the entered numbers in a list
    ele=int(input("Enter the number:"))
    li.append(ele)

print("The list of numbers are:",li)
sum_of_number_list=[]
for i in li:
    sum_number=sum_of_digit(i)
    sum_of_number_list.append(sum_number)
print("The sum of digits of the number present in the list:",sum_of_number_list)




#Enter the number of elements:4
#Enter the number:21
#Enter the number:77
#Enter the number:76
#Enter the number:232
#The list of numbers are: [21, 77, 76, 232]
#The sum of digits of the number present in the list: [3, 14, 13, 7]
