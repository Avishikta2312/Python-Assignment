#Given a string, generate a string of the longest substring of consecutive consonants. If more than one such substring has the same length, the first should appear in the string.


def consecutive_consonant(str):  #return the longest consecutive consonant substring from the string
    current_sequence=""
    longest_sequence=""
    for i in str:
        if (i.isalpha() and i.lower() not in 'aeiou'):     #check whether the character of the string is alphabatic and not vowel
            current_sequence=current_sequence+i            #if yes then add that character in the current sequence
        else:
            if(len(longest_sequence)<len(current_sequence)): #if no then check whether the length of the current sequence is grater than the length of the longest sequence or not
                longest_sequence=current_sequence            #if yes then assing the current sequence to the longest sequence
                current_sequence=""                          #make the current sequence null
    return longest_sequence
str=input("Enter any string:")
print(consecutive_consonant(str))

#Enter any string:program
#pr
