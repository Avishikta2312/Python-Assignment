#Given a list of courses, create a new list of courses that are offered by the department of Computer Applications (i.e., courses that start with MCA]
li=[]
n=int(input("Enter the number of the elements:"))
for i in range(0,n):
    ele=input("enter the course name:")
    li.append(ele)
#print(li)
new_list=[]                           #check wheather in the couse name the word "MCA" is present or not
for i in li:
    if "M" in i:
        if "C" in i:
            if"A" in i:
                new_list.append(i)    #is yes then append it into the new list
print(new_list)

#Enter the number of the elements:5
#enter the course name:MCA1205
#enter the course name:MCA2125
#enter the course name:HUM2191
#enter the course name:MTH2102
#enter the course name:MCA1295
#['MCA1205', 'MCA2125', 'MCA1295']
