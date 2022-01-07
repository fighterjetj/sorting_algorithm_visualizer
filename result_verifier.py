from random_list_generator import gen_list

# Statement for importing the correct sorter (assumes the sort function is named sorter)
from bubble_sort import sorter

# Tests the sorter function (assumes least to greatest)
def verifier():
    rand_list = gen_list(0, 10, 20)
    print("Unsorted list: " + str(rand_list))
    base_list = rand_list.copy()
    test_list = sorter(rand_list)
    base_list.sort()
    print("Base Case: " + str(base_list))
    print("Test Case: " + str(test_list))
    if base_list == test_list:
        print("Success!")
    else:
        print("Error while sorting")


if __name__ == "__main__":
    verifier()
