# list = [1,3,5]
# result = 1
# sonuc = 1
# for i in list:
#     result *= i
#     new_list = str(result)
#     for ii in new_list:
#         sonuc *= int(ii)
# print(sonuc)
    
        


# def multiply(muaz):
#     result = 1
#     for i in muaz:
#         result *= i
#     return result

# multiply(list)

# def persistence(num):
#     if num < 10:
#         return num # Only one digit. Can't iterate over it
#     num_str = str(num)
#     total = 1
#     for i in num_str:
#         total = total * int(i)
#     return 1 + persistence(total)

# print(persistence(1234566))

def persistance(num):
    counter=0
    while num>9:
        counter+=1
        num_str=str(num)
        total=1
        for i in num_str:
            total=total* int(i)
        num=total
    print (counter)

persistance(1)