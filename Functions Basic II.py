# Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list


print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.


def prtRtn(list):
    print(list[0])
    return list[1]


print(prtRtn([5, 7]))

# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def firstPlus(list):

    return list[0]+len(list)


print(firstPlus([1, 2, 3, 4, 5]))

# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]


def greaterThanSec(list):
    val = list[1]
    newList = []
    count = 0
    for i in list:
        if i > val:
            newList.append(i)
            count += 1
    if count < 2:
        return False
    else:
        return newList


print(greaterThanSec([1, 2, 3, 4, 5, 6]))

# Example: length_and_value(4,7) should return [7,7,7,7]


def lenAndVal(len, val):
    list = []
    for i in range(0, len, 1):
        list.append(val)
    return list


print(lenAndVal(4, 7))
