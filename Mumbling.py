# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# Solution-1
def accumm(s):
  return "-".join([(s[i]*(i+1)).title() for i in range(len(s))])

# Solution-2

def accum(item):
    liste = []
    for i in range(len(item)):
        liste.append((item[i]*(i+1)).title())
        
    result = '-'.join(liste)
    return result
        
accum('item')