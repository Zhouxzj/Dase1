L = [1, 2, 3, 4, 5]


def for_to_sort(s):
    for i in range(len(s)):
        for k in range(len(s)):
            if s[i] > s[k]:
                t = s[i]
                s[i] = s[k]
                s[k] = t


for_to_sort(L)
print(L)
