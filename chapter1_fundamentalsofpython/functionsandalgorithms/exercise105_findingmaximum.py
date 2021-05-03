## In this exercise, we will try to find the maximum of an array, or list
## To do this, we wil write a function that returns the index and value of the maximum element within a list


def get_max(my_list):
    running_max_index = 0

    # Iterate over the index-value pairs.
    for index, item in enumerate(my_list):
        if item >= my_list[running_max_index]:
            running_max_index = index
    return running_max_index, my_list[running_max_index]


print(get_max([1, 3, 2]))
print(get_max([1, 3, 56, 29, 100, 99, 3, 100, 10, 23]))
