# Problem: Given two strings check to see if they are anagrams. Anagram is when the two strings can be written using the exact same letters.
# For example:
# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"
def anagram(s1, s2):
    # remove spaces and make lowercase
    s1 = s1.replace(" ", "").lower() 
    s2 = s2.replace(" ", "").lower()
    
    # Return boolean for sorted match.  
    return sorted(s1) == sorted(s2)

print(anagram("clint eastwood", "old west action"))


# doing the same thing with a dictionary
def anagram_dict(s1, s2):
    # remove spaces and make lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # checl if the length of the strings are not equal
    if len(s1) != len(s2):
        return False
    
    # create a dictionary for each string
    count = {}

    for letter in s1: # loop through string 1
        if letter in count:
            count[letter] += 1 # add one to the value
        else:
            count[letter] = 1 # add the letter to the dictionary with a value of 1

    for letter in s2: # loop through string 2
        if letter in count:
            count[letter] -= 1 # subtract one from the value
        else:
            count[letter] = 1 # add the letter to the dictionary with a value of 1  

    for k in count: # loop through the dictionary
        if count[k] != 0: # if the value is not 0
            return False # return false

    return True # return true if all values are 0

    
print(anagram_dict("clint eastwood", "old west action"))