# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
# Examples
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love


sen = "123 fsda? 9897 a dd $½11 3f"
    
def LongestWord(sen):
    import string
    for i in sen:
        if i in string.punctuation or i in string.digits:
            sen = sen.replace(i, "")
    maks = max(sen.split(), key=len)
    return maks


print(LongestWord(sen))

