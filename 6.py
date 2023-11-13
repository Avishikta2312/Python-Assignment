#Accept a string of comma separated 4-digit binary numbers as input and print a comma separated string containing the numbers that are divisible by 3.


str=input("Enter the string:")
li=[]
str=str.replace(","," ")  #replace , with space
li=str.split()
integer_li=[]
for i in range(0,len(li)):        #convert binary number into decimal number
    e=li[i]
    ele=int(e,2)
    integer_li.append(ele)
#print(integer_li)
new_li=[]
for i in range(0,len(integer_li)):     #check which number is divisble bt 3
    ele=integer_li[i]
    if(ele%3==0):
        new_li.append(ele)
new_bi_li=[]
for i in new_li:                 #convert decimal number into binary number
    ele=bin(i)
    ele=ele.replace("0b","")
    new_bi_li.append(ele)
    
print("The numbers that are divisible by 3:",new_bi_li)

#Enter the string:0100, 0011, 1010, 1001 
#The numbers that are divisible by 3: ['11', '1001']

