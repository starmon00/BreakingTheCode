'''
1.8 Assuming you have a method isSubString which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubString
(e.g. "waterbottle" is a rotation of "erbottlewat")
'''

def sub (s1,s2):
    length = len(s1)
    if len == len(s2) and len > 0 :
        s1s1 = s1 + s1
        return isSubString(s1s1, s2)
    return False

    
