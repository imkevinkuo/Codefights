def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
def traverse(arr, swaps, i, visited):
    visited.add(i)
    for j in swaps[i]:
        if j not in visited:
            traverse(arr, swaps, j, visited)
def swapLexOrder(str, pairs):
    swaps = {}
    for pair in pairs:
        if pair[0]-1 not in swaps:
            swaps[pair[0]-1] = set()
        if pair[1]-1 not in swaps:
            swaps[pair[1]-1] = set()
        swaps[pair[0]-1].add(pair[1]-1)
        swaps[pair[1]-1].add(pair[0]-1)
    arr = list(str)
    # loop through indices, traverse to find largest possible letter
    for i in range(0, len(arr)):
        if i in swaps:
            visited = set()
            traverse(arr, swaps, i, visited)
            viable = set(j for j in visited if i != j and not (i < j)^(arr[i] < arr[j]))
            if len(viable) > 0:
                swap(arr,i,max(viable, key=lambda x:arr[x]))
    print(swaps)
    return(''.join(arr))
