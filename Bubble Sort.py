def bubbleSort(list):
    # count = 0
    for j in range(len(list)-1):
        # print("\n\n", "-"*50, "iteration", j)
        for i in range(len(list)-1-j):
            # count += 1
            # print("\n", "*"*80, "\nComparing", list[i], list[i+1])
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                # print("swapped", list[i], list[i+1])
                # print("list now is :", list)
            # else:
                # print("no need to swap", list[i], list[i+1])
    # print("# of evaluation", count)
    return list


print(bubbleSort([1, 5, 3, 2, 0, 8]))
