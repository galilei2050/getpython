

def merge_sort(S):
    n = len(S)
    if n < 2:
        return S

    mid = n // 2

    S1 = S[0:mid]
    S2 = S[mid:n]

    if len(S1) < 25:
        S1 = insert_sort(S1)
    else:
        merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)
    return S


def merge(S1, S2, S):
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

S = [10, 8, 6, 12]
print(merge_sort(S))
assert merge_sort(S) == sorted(S)


def insert_sort(array):
    for i in range(1, len(array)):
        el = array[i]
        j = i
        while j > 0 and array[j-1] > el:
            array[j] = array[j-1]
            j -= 1
        array[j] = el
    return array