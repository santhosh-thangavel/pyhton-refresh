import math

arr  = [10, 11, 17, 11, 34, 21]
first = math.inf
second = math.inf

# print(first)
# print(second)

for i in range(0, len(arr)):
    if arr[i] < first:
        first = arr[i]
        # print(first)

for i in range(0, len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]
print(second)
