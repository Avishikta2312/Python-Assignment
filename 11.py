#Given a string, generate a list of nonempty prefixes of the string, ordered from shortest to longest.


word=input("Enter a word:")
length=len(word)
li=[]

for i in range(1,length+1):
    ele=word[0:i]                #using slicing method we slice the tring and enter the output of the slice fnction into the list
    li.append(ele)
print(li)



#PS D:\python_program> python -u "d:\python_program\ass-2\11.py"
#Enter a word:Banana
#['B', 'Ba', 'Ban', 'Bana', 'Banan', 'Banana']
