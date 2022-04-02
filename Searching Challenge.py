# Searching Challenge
# Have the function SearchingChallenge(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces.

# Examples
# Input: "Hello apple pie"
# Output: Hello
# Input: "No words"
# Output: -1



str = "Today is the greatest day ever."

def letter_counter(str):
    word = []
    count = 1
    for i in str.lower().split(" "):
        for j in i:
            if i.count(j.lower()) > count:
                word = [i]
                count = i.count(j.lower())
    if count == 1:
        return -1
    else:
        return word

print(letter_counter("Today is the greatest day ever."))

