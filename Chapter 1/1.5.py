'''
1.5 Implement a method to perform basic string compressions using the counts of repeated characters.
For example the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.You can assume the string has only upper and lower case letters (a-z).
'''

def string_compression(string):
    answer = ''
    counter = 0
    for num, letter in enumerate(string):
        counter += 1
        if num == len(string)-1:
            answer += (letter + str(counter))
        elif letter != string[num+1]:
            answer += (letter + str(counter))
            counter = 0
    for num in answer[1::2]:
        if num != '1':
            return answer
    return string


print(string_compression("teehee"))
print(string_compression("abc"))
print(string_compression("aabcccccaaa"))
