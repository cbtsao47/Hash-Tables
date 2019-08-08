# Write a function integerPairs to find and print out all pairs of integers within an input array which sum up to a specified input value k.

# There are multiple ways to do this, depending upon whether you want to favor runtime or space.

# Example:

# input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11 

# expected output: '6 5', '7 4', '8 3', '9 2', '10 1'
# Analyze the time and space complexity of your solution.

# def integerPairs(arr,target):
#     for i in range(len(arr)):
#         difference=target-arr[i]
#         for k in range(len(arr)):
#             if difference == arr[k]:
#                 print(f"{arr[i]} {arr[k]}")
def integerPairs(arr,target):
    # create a dictionary cache
    cache = {}
    # go over the arr
    for number in arr:
    #  find the difference, check if the difference exists in the cache
        difference= target-number
        if not difference in cache:
            cache[number]= difference
            print(f"{number}, {difference}")
    # for key in cache:

integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11 )
