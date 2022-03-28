#Find Unique number in List

def find_uniq(arr):
    empt_dict = {}
    for i in arr:
        if str(i) in empt_dict:
            empt_dict[str(i)].append(i)
        else:
            empt_dict[str(i)] = [i]
    muaz = list(empt_dict.values())
    for ii in muaz:
        if len(ii) == 1:
            print(ii[0])

find_uniq([1,1,1,1,2,1,1,1])