def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)



def merge_two_sorted_list(lst1, lst2):
    sorted_lst = []
    ln1 = len(lst1)
    ln2 = len(lst2)
    i = j = 0

    while i < ln1 and j < ln2:
        if lst1[i] <= lst2[j]:
            sorted_lst.append(lst1[i])
            i += 1
        else:
            sorted_lst.append(lst2[j])
            j += 1

    while i < ln1:
        sorted_lst.append(lst1[i])
        i += 1
    
    while j < ln2:
        sorted_lst.append(lst2[j])
        j += 1
    
    return sorted_lst


if __name__ == '__main__':
    arr = [10, 78, 9, 1, 0, 3, 86, 17, 29, 41]
    
    print(merge_sort(arr))