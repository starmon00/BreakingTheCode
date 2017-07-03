'''
1.2 Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string
'''

def reverse(*string):
    answer = []
    for word in string:
        answer.append(word[::-1])
    print(answer)

print(reverse('fdsa'))
print(reverse('aaaa'))
