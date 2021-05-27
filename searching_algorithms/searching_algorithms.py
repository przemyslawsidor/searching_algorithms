import math
import random

# selectAlgorithm function is main loop of the program. It takes a list of numbers and its size.
# Number of algorithm selected by user is checked and if its correct, user enters the value and then the search function is called.
def selectAlgorithm(args, n):
    algorithm_num = int(input("\n1. Linear search\n2.Binary search\n3.Jump Search\n4. Interpolation search\n5. Exponential search\nPlease select algorithm number: "))
    if algorithm_num != 1 and algorithm_num != 2 and algorithm_num != 3 and algorithm_num != 4 and algorithm_num != 5:
        print("\nError\nSelect algorithm number again\n")
        selectAlgorithm(args, n)
    else:
        number = int(input("Please select number: "))
        index = int(search(algorithm_num, numbers, len(numbers), number))
        if index == -1:
            print("\n\nCould not find given number.\n\n")
        else:
            print("\n\nGiven number index is ", index, "\n\n")
        selectAlgorithm(args, n)

# search funtion takes choosen algorithm number, list of numbers, size of list and entered value.
# Depending on the choosen algorithm, correct function is called. Every function returns entered value index.
# If entered value is not found, it returns -1. Then proper message is displayed.
def search(algorithm_num, args, n, x):
    if algorithm_num == 1:
        return linearSearch(args, n, x)
    elif algorithm_num == 2:
        return binarySearch(args, 0, n-1, x)
    elif algorithm_num == 3:
        return jumpSearch(args, x, n)
    elif algorithm_num == 4:
        return interpolationSearch(args, 0, n-1, x)
    elif algorithm_num == 5:
        return exponentialSearch(args, n, x)
    else:
        return -1;

def linearSearch(args, n, x):
    for i in range(0, n):
        if args[i] == x:
            return i
    return -1

def binarySearch(args, left, right, x):
    if right >= left:
        mid = int(left + (right - left) // 2)
        if args[mid] == x:
            return mid
        elif args[mid] > x:
            return binarySearch(args, left, mid-1, x)
        else:
            return binarySearch(args, mid+1, right, x)
    else:
        return -1

def jumpSearch(args, x , n):
    step = math.sqrt(n)
    prev_step = 0
    while args[int(min(step, n)-1)] < x:
        prev_step = step
        step += math.sqrt(n)
        if prev_step >= n:
            return -1

    while args[int(prev_step)] < x:
        prev_step += 1
        if prev_step == min(step, n):
            return -1
        
    if args[int(prev_step)] == x:
        return prev_step

    return -1

def interpolationSearch(args, lowest, highest, x):
    if (lowest <= highest and x >= args[lowest] and x <= args[highest]):
        pos = lowest + ((highest - lowest) // (args[highest]) * (x-args[lowest]))
        if args[pos] == x:
            return pos
        
        if args[pos] < x:
            return interpolationSearch(args, pos + 1, highest, x)

        if args[pos] > x:
            return interpolationSearch(args, lowest, pos - 1, x)
    return -1;

def exponentialSearch(args, n, x):
    if args[0] == x:
        return 0

    i = 1
    while i < n and args[i] <= x:
        i = i * 2

    return binarySearch(args, i/2, min(i, n-1), x)
    
numbers = []
for i in range(20):
    if i == 0:
        numbers.append(random.randint(1,9))
    else:
        numbers.append(numbers[i-1] + random.randint(1,9))

print("Generated numbers: ")
for i in range(20):
    print(i, numbers[i])

selectAlgorithm(numbers, len(numbers))
