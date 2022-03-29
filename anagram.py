"""
Definition of Anagram : a word or phrase made by transposing the letters of another word or phrase.
                   Ex : The word "secure" is an anagram of "rescue."
"""

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


def anagrams(word, words):
    anagram_list = []
    for i in words:
        if (sorted(i)) == (sorted(word)):
            anagram_list.append(i)
    return anagram_list


print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))


# word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]

# # initialize a list
# anagram_list = []
# for word_1 in word_list:
#     for word_2 in word_list:
#         if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
#             anagram_list.append(word_1)
# print(anagram_list)


# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# anagrams = {}

# for i in words:
#    ii = str(sorted(i))
#    if ii in anagrams:
#       anagrams[ii].append(i)
#    else:
#       anagrams[ii] = [i]

# liste= list(anagrams.values())
# print(liste)


# anagram = ["Muaz", "zam", "zamu", "azam"]
# anag = {}
# for i in anagram:
#     element = "".join(sorted(i))
#     if element in anag:
#         anag[element].append(i)
#     else:
#         anag[element] = [i]
#     print(anag.values())
