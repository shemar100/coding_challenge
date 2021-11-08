# Problem: Given two strings check to see if they are anagrams. Anagram is when the two strings can be written using the exact same letters.
# For example:
# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"
def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower() # remove spaces and make lowercase
    s2 = s2.replace(" ", "").lower() # remove spaces and make lowercase
    return sorted(s1) == sorted(s2)

print(anagram("clint eastwood", "old west action"))