# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def bigSize(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = "big"
    return list


print(bigSize([-1, 3, 5, -5]))

# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it


def countPos(list):
    count = 0
    for i in range(0, len(list), 1):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list


print(countPos([-1, 1, 1, 1]))

# Example: sum_total([1,2,3,4]) should return 10


def sumTotal(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum


print(sumTotal([1, 2, 3, 4]))

# Example: average([1,2,3,4]) should return 2.5


def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum/len(list)


print(average([1, 2, 3, 4]))

# Example: length([37,2,1,-9]) should return 4


def length(list):

    return len(list)


print(length([37, 2, 1, -9]))

# Example: minimum([37,2,1,-9]) should return -9


def minimum(list):
    min = list[0]
    for i in range(0, len(list), 1):
        if list[i] < min:
            min = list[i]
    return min


print(minimum([37, 2, 1, -9]))

# Example: maximum([37,2,1,-9]) should return 37


def maximum(list):
    max = list[0]
    for i in range(0, len(list), 1):
        if list[i] > max:
            max = list[i]
    return max


print(maximum([37, 2, 1, -9]))

# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(list):
    dict = {}
    sum = 0
    avg = 0
    min = list[0]
    max = list[0]
    length = len(list)
    for i in range(0, len(list), 1):
        sum += list[i]
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    avg = sum/length
    dict.update({'sumTotal': sum, 'average': avg,
                'minimum': min, 'maximum': max, 'length': length})
    return dict


print(ultimate_analysis([37, 2, 1, -9]))

# second solution for ultimate_analysis


def ultimate_analysis2(list):
    s = sumTotal(list)
    a = average(list)
    m = minimum(list)
    n = maximum(list)
    l = length(list)

    return {
        'sumTotal': s,
        'average': a,
        'minimum': m,
        'maximum': n,
        'length': l
    }


print(ultimate_analysis2([37, 2, 1, -9]))

# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37],Do this without creating a second list


def Reverse(list):
    for i in range(len(list)-1, -1, -1):
        list.append(list.pop(i))
    return list


print(Reverse([37, 2, 1, -9]))

# second solution for reverse using sequence


def Reverse2(list):

    return list[::-1]


print(Reverse2([37, 2, 1, -9]))

# third solution for reverse using reversed method


def Reverse3(list1):

    return list(reversed(list1))


print(Reverse3([37, 2, 1, -9]))

# Fourth solution for reverse using reverse method


def Reverse4(list):
    list.reverse()
    return list


print(Reverse4([37, 2, 1, -9]))
