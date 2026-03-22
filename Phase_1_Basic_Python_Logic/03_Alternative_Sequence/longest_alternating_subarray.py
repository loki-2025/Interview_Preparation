def longest_alternating_subarray(arr):
    l = len(arr)
    max_len = 0
    current_direction = 0
    previous_direction = 0
    if l == 0:
        return 0
    if l == 1:
        return 1
    for i in range(1,l):
        if arr[i] > arr[i-1]:
            current_direction = 1
        elif arr[i] < arr[i-1]:
            current_direction = -1
        else:
            current_direction = 0
        if current_direction == 0:
            current_len = 1
        elif previous_direction == 0:
            current_len = 2
        elif previous_direction != current_direction:
            current_len += 1
        else:
            current_len = 2
         
        max_len = max(max_len, current_len)
        previous_direction = current_direction
    return max_len