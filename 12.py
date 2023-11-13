#Given a list of filenames, generate a new list to rename all the files with extension ‘cpp’ to the extension ‘h’.


li=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=input("Enter the file name:")
    li.append(ele)
   
file_extension=".cpp"
new_list=[] 
for i in li:
    if file_extension in i:          #check weather extension .cpp present in the file name
        ele=i.replace(".cpp",".h")   #if yes then replace .cpp extension with .h extension and enter the file name with new extention in the list
        new_list.append(ele)
    else:
        new_list.append(i)
print(new_list)

#PS D:\python_program> python -u "d:\python_program\ass-2\12.py"
#Enter the number of elements:6
#Enter the file name:program.c
#Enter the file name:stdio.cpp
#Enter the file name:sample.cpp
#Enter the file name:a.out
#Enter the file name:math.cpp
#Enter the file name:cpp.out
#['program.c', 'stdio.h', 'sample.h', 'a.out', 'math.h', 'cpp.out']
