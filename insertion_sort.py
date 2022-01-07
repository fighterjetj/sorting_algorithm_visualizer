# Insertion Sort
# The way insertion sort works is it iterates through the array, comparing each item with the item before.
# If the item before is greater, the two items are switched.  The comparison repeats until they
# aren't switched.  Then the process is repeated with the next item in the array.

# Implementation of insertion sort (not step by step)
def insertion_sorter(array):
    for i in range(1, len(array)):
        curr_ind = i
        while (curr_ind > 0) and array[curr_ind - 1] > array[curr_ind]:
            array[curr_ind - 1], array[curr_ind] = array[curr_ind], array[curr_ind - 1]
            curr_ind -= 1


class Sorter:
    def __init__(self, array):
        self.array = array
        if len(array) <= 1:
            raise Exception("The array must be larger than one item")
        self.orig_ind = 1
        self.curr_ind = 1

    def get_array(self):
        return self.array

    def next_step(self):
        # If we have iterated through the array, then the original index value will be past the end of the array
        if self.orig_ind >= len(self.array):
            return []
        # If we are at the end, we can move on to the next value
        if self.curr_ind == 0:
            self.orig_ind += 1
            self.curr_ind = self.orig_ind
            return [self.curr_ind]
        # Seeing if the values should be switched
        if self.array[self.curr_ind - 1] > self.array[self.curr_ind]:
            self.array[self.curr_ind - 1], self.array[self.curr_ind] = (
                self.array[self.curr_ind],
                self.array[self.curr_ind - 1],
            )
            self.curr_ind -= 1
        # Moving onto the next value if we don't need to switch
        else:
            self.orig_ind += 1
            self.curr_ind = self.orig_ind
        return [self.curr_ind]


# Test code
if __name__ == "__main__":
    # Simple test code
    import random_list_generator

    rand_array = random_list_generator.gen_list(0, 100, 20)
    rand2 = rand_array[:]
    print(rand_array)
    test_pointer = Sorter(rand_array)
    for i in range(1000):
        test_pointer.next_step()
    rand2.sort()
    print(test_pointer.get_array())
    print(rand2)
    if test_pointer.get_array() == rand2:
        print("sorted")
