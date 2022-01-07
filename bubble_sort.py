# Bubble Sort
# The way bubble sort works is that it compares two adjacent elements, and switches them if they're out of order
# Repeats this process through the entire array, repeating until no swaps are made

# Sorts using bubble sort without recursion
def bubble_sorter(array):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                swapped = True
                array[index], array[index + 1] = array[index + 1], array[index]
    return array


# Sorts using bubble sort with recursion
def recursive_bubble_sorter(array):
    if len(array) == 1:
        return array
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]
    return_list = []
    return recursive_bubble_sorter(array[:-1]) + [array[-1]]


# Pointer class for the visualizer
class Sorter:
    def __init__(self, array):
        self.array = array
        self.curr_ind = 1
        self.since_swap = 0
        self.iter = 0

    def get_array(self):
        return self.array

    # Function for advancing to the next step, returning the index of the item being currently looked at
    def next_step(self):
        # Only advances to the next step in the process if it hasn't finished
        if self.since_swap < len(self.array) - 2:
            # Swaps the current index and the index behind it if the index behind is greater
            if self.array[self.curr_ind] < self.array[self.curr_ind - 1]:
                self.array[self.curr_ind], self.array[self.curr_ind - 1] = (
                    self.array[self.curr_ind - 1],
                    self.array[self.curr_ind],
                )
                self.since_swap = 0
            else:
                self.since_swap += 1
            # Moves onto the next item in the list
            self.curr_ind += 1
            # Resets the variables once they are at the end of the list
            if self.curr_ind >= len(self.array) - self.iter:
                self.curr_ind = 1
                self.since_swap = 0
                self.iter += 1
        else:
            # Returns an empty list once the sorting is done
            return []
        return [self.curr_ind]


if __name__ == "__main__":
    # Just some simple test code
    import random_list_generator

    rand_array = random_list_generator.gen_list(0, 100, 20)
    print(rand_array)
    pointer = Sorter(rand_array)
    for i in range(1000):
        pointer.next_step()

    print(pointer.get_array())
    rand_array.sort()
    print(rand_array)
    print(rand_array == pointer.get_array())
