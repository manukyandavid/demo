ls = [4, -8, 6, 78, -7, -16, 0, 1, 1]


def max_of_list(lst):
    max_item = lst[0]
    for i in lst:
        if i > max_item:
            max_item = i

    return max_item


print(max_of_list(ls))