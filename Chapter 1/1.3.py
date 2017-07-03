'''
1.3 Given two strings, write a method to decide if one is a permutation of the other.
'''

def permutation(string1, string2):
    if len(string1) == len(string2):
        for letter in string1:
            if string1.count(letter) != string2.count(letter):
                return False
        return True
    return False

print(permutation('a','a'))
print(permutation('abc','bca'))
print(permutation('aa','ab'))
print(permutation('',''))


