def selectionSort(list):
    for i in range(0, len(list)-1):
        print("i", i)
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        if min != i:
            print("min", min)
            list[i], list[min] = list[min], list[i]
            print("list", "*"*50, list)
    return list


print(selectionSort([7, 4, 9, 1, 0, 8, 2, 5, 3, 6, 9]))
