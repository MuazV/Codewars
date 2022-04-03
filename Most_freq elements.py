# Given a list, return the most frequent (repeating) element.
# Note : If there are the same number of repeating elements, it returns the first element that repeats most from left to right in the list.

# For example:

# Test	Result
# print(most_freq([1,2,3,3,3,3,4,4,5,5])) 
# 3
# print(most_freq([1,1,2,3,3])) 
# 1
# print(most_freq([3,1,2,1,3])) 
# 3

def most_freq(given_list) :
    liste = []
    for i in given_list:
        liste.append(i)
    sonuc = liste.count(max(liste, key = liste.count))
    
    if sonuc > 1 :
        return (max(liste, key=liste.count))
    else :
        return 0

# print(most_freq([1,2,3,3,1]))

