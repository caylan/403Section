def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        low = i
        for j in range(i + 1, n):
            if lst[j] < lst[low]:
                low = j
        lst[i], lst[low] = lst[low], lst[i]
    return lst