# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# string = "the-stealth-warrior"
# a, b, c = string.split("-")
# liste = [a,b.title(),c.title()]
# empty_str = ""
# for i in liste:
#     empty_str += i



# a = "the-stealth-warrior"
# a = "The_Stealth_Warrior-"
# y = ""
# for i in a:
#   if i.isalpha():
#     y += i
#   else:
#     y += " "
# print(y)
# print((y[:1]+y.title()[1:]).replace(" ",""))

def to_camel_case(text):
    y= ""
    for i in text:
        if i.isalpha():
            y += i
        else:
            y += " "
    return ((y[:1] + y.title()[1:]).replace(" ", ""))

print(to_camel_case("the_stealth_warrior"))
