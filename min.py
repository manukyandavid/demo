ls = [4, -8, 6, 78, -7, -16, 0, 1, 1]


def min_of_list(lst):
    min_item = lst[0]
    for i in lst:
        if i < min_item:
            min_item = i

    return min_item


print(min_of_list(ls))