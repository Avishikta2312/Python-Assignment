#A list contains the roll nos. of students of MCA 1st and 2nd year who enrolled in the debate club. The roll no. of the students is prefixed with the year (2 digits) of admission. From that given list, create two separate lists for 1st year students and 2nd year students.

li=[2182001,2182023,2282022,2282056,2182049,2282036,2182053]
li=map(str,li)                                               #converting the list of integer into list of string
first_list=[]
second_list=[]
for i in li:
    check=i[0:2]                                             #if the first two digit of the roll number is 22 then append the number into first year
    if(check=="22"):
        first_list.append(i)
    else:                                                    # otherwise append the rool number into second year
        second_list.append(i)
print("First year:",first_list)
print("Second year:",second_list)



#First year: ['2282022', '2282056', '2282036']
#Second year: ['2182001', '2182023', '2182049', '2182053']