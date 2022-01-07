# Merge Sort
# The way merge sort works is the list is divided in half over and over again in a recursive process,
# until it has been subdivided into each individual list item.  It then compares the first item in each list,
# putting the one that is lesser or greater (depending on if the list is being sorted ascending or descending)
# into a new list, repeating that process until one list is empty, at which point the other list can be appended,
# and the process repeats with larger and larger sub-lists until it's at the final list

# Implementation of merge sort not intended to be done step by step
def merge_sorter(array):
    # If the array has a length of 1, no sorting is necessary
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        # Getting the sorted halves of the array
        first_array = merge_sorter(array[:mid])
        second_array = merge_sorter(array[mid:])
        result = []
        # Looping through the lists until one of them is empty
        while len(first_array) > 0 and len(second_array) > 0:
            if first_array[0] > second_array[0]:
                result.append(second_array.pop(0))
            else:
                result.append(first_array.pop(0))
        # Appending the list that isn't empty to the resulting list
        if len(first_array) == 0:
            result += second_array
        else:
            result += first_array
        return result


# Pointer class for the visualizer (designed to show how it works step by step)
class Sorter:
    # Initializes the object - array must have more than one item
    def __init__(self, array):
        if len(array) < 2:
            raise Exception("The length of the array must be greater than 1")
        self.array = array
        self.sorted = False
        # Stores whether or not we are on the first pass
        self.first_pass = True
        self.subdivisors = [len(array)]
        # Loop that runs until only 1s and 2s remain in the list
        # The boolean works because on each iteration, we split each item on the list
        # This effectively halves each item, repeating until the list average is less than 2
        # An average of less than 2 would mean each item is a 1 or a 2
        while (sum(self.subdivisors) * 1.0) / (len(self.subdivisors) * 1.0) > 2:
            currInd = 0
            # Iterates through the list.  The current index must be tracked seperately
            # This is b/c we are inserting items into the list as we iterate through it
            for i in range(len(self.subdivisors)):
                # If the value is 1 or 2, no change is needed
                if self.subdivisors[currInd] > 2:
                    # Removes the current value
                    currVal = self.subdivisors.pop(currInd)
                    # Gets the 2 integer halves that make up the value
                    val1 = int(currVal / 2)
                    val2 = currVal - val1
                    self.subdivisors.insert(currInd, val2)
                    self.subdivisors.insert(currInd, val1)
                    currInd += 2
                    # left = not left
                else:
                    currInd += 1
        self.sub_size = self.subdivisors[:]
        # Iterates through the list and makes each value into the start index for its part of the list
        for i in range(len(self.subdivisors)):
            self.subdivisors[len(self.subdivisors) - i - 1] = sum(
                self.subdivisors[: len(self.subdivisors) - i - 1]
            )
        # print(self.sub_size)
        # Stores the index of the current subarray at and the index in the subarray being looked at
        # first_sub[0] is the index of the subarray and first_sub[1] is the index in the array overall
        self.first_sub = [0, 0]
        self.second_sub = [1, self.subdivisors[1]]
        self.last_highlighted = []

    def get_array(self):
        return self.array

    def get_divisors(self):
        return self.subdivisors

    # Will iterate forward and then backwards through the array to prevent one half from becoming much smaller than the other half
    # Ex: sorts each pair except for the last one, which has no pair.  On the second
    def next_step(self):
        # If on the first pass, must sort the unsorted pairs
        if self.first_pass:
            # print("First pass")
            # If past the last value, know the first pass is done
            if self.first_sub[0] == len(self.subdivisors):
                self.first_pass = False
                self.first_sub = [0, 0]
                self.last_highlighted = [0]
                return self.last_highlighted
            # If not a pair, just move to the next value
            elif self.sub_size[self.first_sub[0]] == 1:
                self.first_sub[0] += 1
                self.last_highlighted = [self.subdivisors[self.first_sub[1]]]
                return self.last_highlighted
            else:
                curr_ind = self.subdivisors[self.first_sub[0]]
                # If a pair and out of order, switch the two
                if self.array[curr_ind] > self.array[curr_ind + 1]:
                    self.array[curr_ind], self.array[curr_ind + 1] = (
                        self.array[curr_ind + 1],
                        self.array[curr_ind],
                    )
                self.first_sub[0] += 1
                self.last_highlighted = [curr_ind]
                return self.last_highlighted
        # No need for an else statement because if it's the first pass, the returns will prevent this part from running
        # Checking if the list is sorted
        if self.sorted:
            return []
        # Checking if the list needs to loop back to the start - first bool is to check we are at the array end,
        # second bool is to check if we are at the end of either subarray
        if (self.second_sub[0] + 1 >= len(self.subdivisors)) and (
            (self.first_sub[1] == self.second_sub[1])
            or (self.second_sub[1] == len(self.array))
        ):
            # Checking if we finished sorting the array
            # If we are at the end of the array and there are only 2 subdivisions, sorting has finished
            if len(self.subdivisors) <= 2:
                self.sorted = True
                return self.last_highlighted
            else:
                x = self.sub_size.pop(-1)
                self.sub_size[-1] += x
                self.subdivisors.pop(-1)
                self.first_sub = [0, 0]
                self.second_sub = [1, self.subdivisors[1]]
                self.last_highlighted = [self.first_sub[1], self.second_sub[1]]
                return self.last_highlighted
        # Checking if we need to move onto the next subdivision (but not loop back over)
        if (
            self.second_sub[1]
            == self.subdivisors[self.second_sub[0]] + self.sub_size[self.second_sub[0]]
        ) or (self.first_sub[1] == self.second_sub[1]):
            self.subdivisors.pop(self.second_sub[0])
            self.sub_size[self.first_sub[0]] += self.sub_size.pop(self.second_sub[0])
            self.first_sub[0] += 1
            self.second_sub[0] += 1
            self.first_sub[1] = self.subdivisors[self.first_sub[0]]
            self.second_sub[1] = self.subdivisors[self.second_sub[0]]
        # Moving forward
        if self.array[self.first_sub[1]] > self.array[self.second_sub[1]]:
            self.array.insert(self.first_sub[1], self.array.pop(self.second_sub[1]))
            self.first_sub[1] += 1
            self.second_sub[1] += 1
        else:
            self.first_sub[1] += 1
        self.last_highlighted = [self.first_sub[1], self.second_sub[1]]
        return self.last_highlighted


if __name__ == "__main__":
    # Simple test code
    import random_list_generator

    rand_array = random_list_generator.gen_list(0, 100, 29)
    rand2 = rand_array[:]
    print(rand_array)
    print(merge_sorter(rand_array))
    rand_array.sort()
    print(rand_array)
    test_pointer = Sorter(rand2)
    # print(test_pointer.get_divisors())
    # for i in range(10000):
    # print(test_pointer.next_step())
    i = 0
    for i in range(1000):
        test_pointer.next_step()
    print(test_pointer.get_array())
    print(rand_array)
