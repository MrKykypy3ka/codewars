def max_sequence(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result = max(sum(arr[i:j + 1]), result)
    return result


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
