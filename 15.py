#Given a list of names, generate a list where each element is the surname of the corresponding element in the input list.


li=["A Prasad Sen","Ananth B Chand","Heers Juhuri","Tapasi Das","Gambhir Mudi"]
surname_list=[]
for i in li:
    new_list=i.split()           #convert each string into a list of string
    length=len(new_list)
    ele=new_list[length-1]       #assing the last element of the list into ele variable
    surname_list.append(ele)
print(surname_list)



#['Sen', 'Chand', 'Juhuri', 'Das', 'Mudi']