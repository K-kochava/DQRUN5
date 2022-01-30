from random import seed
from random import randint
seed(1)


def create_random_list(size):
    new_list = []
    for value in range(size):
        value = randint(0, 1000)
        new_list.append(value)
    return new_list


def sorting(arr):
    n = len(arr)

    for i in range(n - 1):

        for k in range(0, n - i - 1):

            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


def odd_number(arr):
    odd_total = 0
    odd_count = 0

    for i in arr:

        if (i % 2 != 0):
            odd_total = odd_total + i
            odd_count = odd_count + 1
            print(i)
    try:
        return odd_total/odd_count
    except:
        print("An exception occurred")


def even_number(arr):
    even_total = 0
    even_count = 0

    for i in arr:

        if (i % 2 != 0):
            even_total = even_total + i
            even_count = even_count + 1
    try:
        return even_total/even_count
    except:
        print("An exception occurred")


a = create_random_list(100)
print(odd_number(sorting(a)))
print(even_number(sorting(a)))