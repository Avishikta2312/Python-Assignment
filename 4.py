#Format input names, given as strings, as follows
#Sample
#Input                          Output
#Aryadev                       Aryadev
#Rajsekhar Basu                 R. Basu
#Nabaneeta Dev Sen             N. D. Sen
#Dawlat Wazir Bahram Khan     D. W. B. Khan



str=input("Enter your full name:")
li=str.split()                    #split function is use to convert a string into a list
n=len(li)-1                       #len function is use to find thelength of the list
for i in range(0,n):
    word=li[i]                    #in the word variable we store the element of the list
    print(word[0:1],end="")        #using string slicing we print the first letter of the each element of the list without the last element
    print(". ",end="")
print(li[n])                      #print the last element of the list

#set1
#Enter your full name:Rajsekhar Basu
#R. Basu

#set2
#Enter your full name:Dawlat Wazir Bahram Khan
#D. W. B. Khan

