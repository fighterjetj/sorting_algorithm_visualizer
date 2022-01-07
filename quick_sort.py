# Quick Sort
# The way quick sort works is you select a pivot value (in this case the first value in the list),
# and sorting the list so that every value greater than the pivot is to one side of it,
# and every value less than the pivot is on the other side, which repeats with each sublist on either side

# Implementation of quick sort (not step by step)
def quick_sorter(array):
    # Base case
    if len(array) <= 1:
        return array
    # Declaring the pivot value and the index where it'll go to divide the list
    pivot_val = array[-1]
    pivot_place = 0
    # Sorting above/below the pivot
    for i in range(len(array) - 1):
        # If the value should be below the pivot value, is moved there
        if array[i] < pivot_val:
            array.insert(0, array.pop(i))
            pivot_place += 1
    array.insert(pivot_place, array.pop(-1))
    less_pivot = array[:pivot_place]
    greater_pivot = array[pivot_place + 1 :]
    return quick_sorter(less_pivot) + [pivot_val] + quick_sorter(greater_pivot)


class Sorter:
    # Initializer
    def __init__(self, array):
        self.array = array
        # Because the range of the subarrays will be dependent on the finished pivots, non-inclusive,
        # we add the -1 and len(array) to act as bounds for the entire array b/c it will be non-inclusive
        self.finished_pivots = [-1, len(array)]
        # Index of the start pivot IN THE FINISHED PIVOT ARRAY
        self.start_pivot_ind = 0
        # Current index being looked at and the index of where the pivot is set to go IN THE ARRAY
        self.curr_ind = 0
        self.pivot = 0

    def get_array(self):
        return self.array

    def next_slice(self):
        # If the distance between pivots is 1, we know we don't need to do any pivoting
        for i in range(len(self.finished_pivots) - 1):
            if (self.finished_pivots[i + 1] - self.finished_pivots[i]) == 2:
                self.finished_pivots.insert(i, self.finished_pivots[i] + 1)
        if len(self.finished_pivots) == len(self.array) + 2:
            return []
        # Finding the next subarray that is longer than just one item
        fin = False
        next_start_pivot = self.start_pivot_ind + 1
        for i in range(next_start_pivot, len(self.finished_pivots) - 1):
            if (self.start_pivot_ind[i + 1] - self.start_pivot_ind[i]) > 2:
                self.start_pivot_ind = i
                self.curr_ind = self.start_pivot_ind[i] + 1
                self.pivot = self.start_pivot_ind[i] + 1
                fin = True
        if fin:
            for i in range(next_start_pivot - 1):
                if (self.start_pivot_ind[i + 1] - self.start_pivot_ind[i]) > 2:
                    self.start_pivot_ind = i
                    self.curr_ind = self.start_pivot_ind[i] + 1
                    self.pivot = self.start_pivot_ind[i] + 1

    def next_step(self):
        # If the list is sorted
        if len(self.finished_pivots) == len(self.array) + 2:
            return []
        # If at the end of the subarray
        if self.curr_ind == self.finished_pivots[self.start_pivot_ind + 1]:
            # Adding the new finalized pivot location
            self.finished_pivots.insert(self.start_pivot_ind + 1, self.pivot)
            if len(self.finished_pivots) == len(self.array) + 2:
                return []
            # The next pivot index in the finished pivot location list is 2 forward because of the added one
            self.start_pivot_ind += 2
            # Looping it back over if past the end of the list
            self.start_pivot_ind = self.start_pivot_ind % (
                len(self.finished_pivots) - 1
            )
            x = 0
            # Makes it so we skip all the pivots with no subarrays betwee
            while (
                self.finished_pivots[self.start_pivot_ind] + 1
                == self.finished_pivots[
                    (self.start_pivot_ind + 1) % len(self.finished_pivots)
                ]
            ):
                x += 1
                self.start_pivot_ind += 1
                self.start_pivot_ind = self.start_pivot_ind % (
                    len(self.finished_pivots) - 1
                )
            self.curr_ind = self.finished_pivots[self.start_pivot_ind] + 1
            self.pivot = self.curr_ind
        pivot = self.array[self.pivot]
        if self.array[self.curr_ind] < pivot:
            self.array.insert(self.pivot, self.array.pop(self.curr_ind))
            self.pivot += 1
        self.curr_ind += 1
        return [self.curr_ind, self.pivot]


if __name__ == "__main__":
    # Simple test code
    import random_list_generator

    rand_array = random_list_generator.gen_list(0, 100, 20)
    rand2 = rand_array[:]
    print(rand_array)
    rand2.sort()
    test_pointer = Sorter(rand_array)
    x = 0
    while len(test_pointer.next_step()) > 0:
        x += 1
        print(x)
        if x > 1000:
            print("BREAKING")
            break
    print(test_pointer.get_array())
    print(rand2)
