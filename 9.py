#Move a specified element to the end of a list.


li=[]

n=int(input("Enter the number of word:"))
for i in range(0,n):                     #enter the elements in a list
    ele=input("Enter the word:")
    li.append(ele)

word=input("Enter the word that you want to shift in the last:")

if word in li:                           #check whether the entered element are present in the list or not
    li.remove(word)                      #if yes then remove that element from the exsisting list and entered that word in the last
    li.append(word)
    print(li)
else:
    print("The entered word not in the list")
    
#Enter the number of word:6
#Enter the word:Bsc
#Enter the word:Msc
#Enter the word:Btech
#Enter the word:Mtech
#Enter the word:Blib
#Enter the word:Mlib
#Enter the word that you want to shift in the last:Mtech
#['Bsc', 'Msc', 'Btech', 'Blib', 'Mlib', 'Mtech']
