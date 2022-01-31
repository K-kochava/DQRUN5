from random import randint #import of function random(), which generates a random float


def create_random_list(size): # creation of function that generates list with size that is defined when called.
    new_list = [] #creation of empty range
    for value in range(size): #iteration of each variable for number of items=size.
        value = randint(0, 1000) #variable is assigned from range from 0 to 1000.
        new_list.append(value) #all generated values are added to the empty range.
    return new_list #range is returned.


def sorting(arr):# creation of function that sorts list.
    n = len(arr) #variable of size of items.
    for i in range(n - 1): #iteration of each variable for number of items=size-1 (because it starts with 0).
        for k in range(0, n - i - 1): #assign last elemnt.
            if arr[k] > arr[k + 1]:#validation of current variant with next one and ...
                arr[k], arr[k + 1] = arr[k + 1], arr[k]#...change element place if next is greater.
    return arr #return of sorted array.


def odd_number(arr): #creation of function that summs up, counts average for odd numbers.
    odd_total = 0 #Creation of variable that has summ of odd numbers.
    odd_count = 0 #Creation of variable that has number of odd numbers.

    for i in arr:# Iteration of each variable in a range.
        if (i % 2 != 0):#Condition if variable has remainder after being split by 2 (if it is not equal to 0 - then odd).
            odd_total = odd_total + i#variable that has sum of odd numbers. Each odd number is added starting from initial odd_total = 0.
            odd_count = odd_count + 1#variable that has number of odd numbers. For each odd number 1 is added starting from initial odd_count = 0.
    try: #block for handling exceptions.
        return odd_total/odd_count #Return of average of odd numbers. total sum of odd numbers/total number of odd count.
    except: #If the return expression did not work as expected...
        print("An exception occurred") #...error message should be printed.


def even_number(arr):  #creation of function that summs up, counts average for even numbers.
    even_total = 0 #Creation of variable that has summ of even numbers.
    even_count = 0 #Creation of variable that has number of even numbers.

    for i in arr:# Iteration of each variable in a range.
        if (i % 2 == 0):#Condition if variable has 0 remainder after split by 2 -then even.
            even_total = even_total + i #variable that has sum of even numbers. Each even number is added starting from initial even_total = 0.
            even_count = even_count + 1 #variable that has number of even numbers. For each even number 1 is added starting from initial even_count = 0.
    try:#block for handling exceptions.
        return even_total/even_count #Return of average of odd numbers. total sum of odd numbers/total number of odd count.
    except: #If the return expression did not work as expected...
        print("An exception occurred")#...error message should be printed.


a = create_random_list(100) #Creation of variable with random list.
print("Average for odd numbers in range is", odd_number(sorting(a)),".") #Print of odd average.
print("Average for even numbers in range is", even_number(sorting(a)),".") #Print of even average.