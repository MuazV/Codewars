# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "()[]{}"
# Output: True
# Example 3:
# Input: "(]"
# Output: False
# Example 4:
# Input: "([)]"
# Output: False
# Example 5:
# Input: "{[]}"
# Output: True


s = "{[{]}"                              # ( = 40, ) = 41, [ = 91, ] = 93, { = 123, }= 125


if -2 <= (ord(s[0]) - ord(s[-1])) < 0:
    print(True)
else:
    for i in range(0,len(s)-1):
        if (ord(s[i]) + 1) == ord(s[i+1]):
            print(True)
            break
        elif (ord(s[i]) + 2) == ord(s[i+1]):
            print(True)
            break
        else:
            print(False)
            break
   

















# if string[0] == string[-1]:
#     print(True)
# elif:
#     for i in string:
#         if 
