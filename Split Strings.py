

s = 'abcdefg'
if len(s) % 2 == 0:
    print([s[idx:idx+2] for idx,val in enumerate(s) if idx%2 == 0])
else:
    x = s + "-"
    print([x[idx:idx+2] for idx,val in enumerate(x) if idx%2 == 0])



























