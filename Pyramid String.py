# Question 1: (15 points)
# Write a function named `pyramid(s)` that takes a string as its input
# and PRINTs out a pyramid on the screen based on this string. For example,
# when called as `pyramid("BURKAY")` it will print:
# B
# UU
# RRR
# KKKK
# AAAAA
# YYYYYY
# """
# def pyramid(s):
#  # remove the following line to solve this question
#  return
# """

name = "BURGER"
for i in range(len(name)):
    if i == 0:
        print(name[0])
    else:
        print(name[i]*(i+1))



def pyramid(s):
    for i in range(len(s)):
        if i == 0:
            print(s[0])
        else:
            print(s[i]*(i+1)) 
    
pyramid("BURGER")
        