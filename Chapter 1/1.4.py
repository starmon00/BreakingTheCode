'''
1.4 Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end of the string to hold the additional chracters,
and that you are given the "true" length of the string.

EXAMPLE

Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
'''

def replacement(string, length):
    string = string[:length]
    return string.replace(' ', '%20')

print(replacement('Mr John Smith    ',13))
print(replacement('Mr John Smith    ',5))
print(replacement('Mr John Smith    ',0))
print(replacement('Mr John Smith    ',20))


