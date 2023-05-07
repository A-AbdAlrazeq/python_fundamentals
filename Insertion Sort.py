def insertion_Sort(list):
    for i in range(1, len(list)):
        j = i
        while list[j-1] > list[j] and j > 0:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1
    return list


print(insertion_Sort([1, 6, 4, 8, 9, 3, 1, 5, 7]))
