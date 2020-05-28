from heapq import heappush, heappop


def median_sum(data_file):
    """A function to calculate the median on every iteration
    and add that value to the variable sum_of_medians"""
    with open(data_file, "r") as data_list:
        ## Initialize the elements
        first_element = int(data_list.readline().strip())
        sum_of_medians = first_element
        min_heap = []
        max_heap = []
        heappush(max_heap, first_element)

        for line in data_list:
            ## Extract elements for the data list and add it where correspond in the heaps
            new_item = int(line.strip())
            if new_item <= max_heap[0]:
                heappush(min_heap, -new_item)
            else:
                heappush(max_heap, new_item)
            ## Balancing the heaps for maintain the median invariant in min_heap[0]
            if (len(min_heap) - len(max_heap)) > 1:
                heappush(max_heap, -heappop(min_heap))
            if (len(min_heap) - len(max_heap)) < 0:
                heappush(min_heap, -heappop(max_heap))
            ## Adding the new median to the sum of medians
            sum_of_medians += -min_heap[0]

    return sum_of_medians


file_name = "Median.txt"
median = median_sum(file_name)
four_digit_median = median % 10000
print("The sum of medians is: ", median)
print("The last four digits: ", four_digit_median)
