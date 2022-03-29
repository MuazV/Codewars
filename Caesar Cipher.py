# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.
#(ASCII)
import string

def rot13(message):
    new_list = []
    a = list("abcdefghijklmnopqrstuvwxyz")
    b = list("abcdefghijklmnopqrstuvwxyz".upper())
    for i in message:
        if i in a:
            new_list.append(a[(a.index(i)+13) % ((len(a)))])
        elif i in b:
            new_list.append(b[(b.index(i)+13) % ((len(b)))])
        else:
            new_list.append(i)
    return "".join(new_list)

print(rot13("test"))   
print(rot13("Test"))    







# def rot13(message):
#     new_list = []
#     for i in message:
#         if i in string.ascii_letters:
#             new_list.append(chr(ord(i)+13)) # ek olarak stringlerin 122 den sonrasını almamasını sagla
#         else:
#             new_list.append(i)
#     return "".join(new_list)

# print(rot13("muaz"))


# print(ord("b"))
