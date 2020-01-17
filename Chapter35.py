def twoStrings(S1, S2):
    for i in s1:
        if i in s2:
            return 'Yes'
        else:
            return 'No'
        

s1 = input('Input first str : ')
s2 = input('Input second str : ')
print(twoStrings(s1, s2))