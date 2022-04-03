# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
# Examples
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse


def smallestCommonPart(my_list):
    lengt = len(my_list[1])
    while True:
      for i in range(len(my_list[0])-lengt+1):
        a = my_list[0][i:i+lengt]
        b = list(my_list[1])
        for j in a:
          if j in b:
            b.remove(j)
        if len(b) == 0:
          return my_list[0][i:i+lengt]
      lengt += 1
my_list = ["ahffaksfajeeubsne", "jefaa"]
my_list = ["aaffhkksemckelloe", "fhea"]
print(smallestCommonPart(my_list))