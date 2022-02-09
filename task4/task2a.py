from random import randrange # import of generator of range
import random#import of random function
import string #import of string function


mincount = 2
maxcount = 10
minrange = 0
maxrange = 100
sep = '_'


def create_list_range(mincount = 2, maxcount = 10, minrange = 0, maxrange = 100):
    ls_dict = []  # creating empty list
    k = randrange(mincount, maxcount)  # creating count of dictionaries = random number from 2 to 10
    for n in range(k):  # iteration of dictionaries within range
        my_dict = {random.choice(string.ascii_letters): randrange(minrange, maxrange) for i in range(
            n + 1)}  # create dictionary with key of randomly generated letter and value of randomly generated number
        ls_dict.append(my_dict)  # add each new dictionary to the list
    return ls_dict


def create_key(list_dict, exp_key, exp_value): #new function that will create id for dictionary
    i = 1 #new value that will be assigned to dictionary
    for h in list_dict: # check within each dictionary
        for c in h: #check for each key in dictionary
            if c == exp_key and h[c] == exp_value: #if key matches with expected key and value matches expected value
                return i #return number of dictionary
        i = i + 1 #increase for each new dictionary


def create_new_range(list_dict, sep):
    new_dict = {} #create new final dictionary
    del_list = [] #create new list that should store values to delete
    for y in list_dict: #for each dictionary in the list...
        for key in y: #for each key in dictionary...
            if len(new_dict) != 0 and key in new_dict:#if the key is in multiple sets and ...
                if new_dict[key] > y[key]: #if key from new dictionary has value higher than old
                    new_key = key + sep + str(create_key(list_dict, key, new_dict[key])) #generate new key with key+dict id and higher value
                    new_dict[new_key] = new_dict[key]#add key with higher value to new dictionary
                    del_list.append(key) #add key with lower value to deletion list
                else: #if key from new dictionary has value lower than old
                    new_key = key + sep + str(create_key(list_dict, key, y[key]))  #generate new key with key+dict id and higher value
                    new_dict[new_key] = y[key] #add key with higher value to new dictionary
                    del_list.append(key) #add key with lower value to deletion list
            else: #if the key is unique, ...
                new_dict[key] = y[key] #.. add it as is with value
    for s in set(del_list):  # check each unique value in del_list
        del new_dict[s]  # delete all pairs from new_dict if key is in del_list
    return new_dict


first_range = create_list_range(mincount, maxcount, minrange, maxrange)
second_range = create_new_range(first_range, sep)


print('Task 1 is:' + str(first_range) + '.')
print('Task 2 is:' + str(second_range) + '.')