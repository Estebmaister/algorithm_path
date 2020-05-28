"""
Compute the number of target values t in the interval [-10000, 10000] (inclusive) 
such that there are distinct numbers x, y in the input file that satisfy x + y == t.
For the record of the targets the hash table is a dictionary from py
"""
import time

start_time = time.time()

file_name = "algo-prob-2sum.txt"
with open(file_name) as data_list:
    data_array = sorted([int(data) for data in data_list])

t = dict()
suma = 0
init_pointer = 0
final_pointer = len(data_array) - 1
interval = 10000  # [-10000, 10000]

while init_pointer <= final_pointer:
    if data_array[init_pointer] + data_array[final_pointer] < -interval:
        init_pointer += 1
    elif data_array[init_pointer] + data_array[final_pointer] > interval:
        final_pointer -= 1
    else:
        suma = data_array[init_pointer] + data_array[final_pointer]
        t[suma] = t.get(suma, True)

        for index in range(0, final_pointer - init_pointer):
            suma = data_array[init_pointer] + data_array[final_pointer - index]
            if suma < -interval:
                break
            t[suma] = t.get(suma, True)

        init_pointer += 1

print("--- %.3f seconds ---" % (time.time() - start_time))

print("%s target values t in the interval" % len(t))
