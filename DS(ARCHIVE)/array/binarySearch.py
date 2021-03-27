## Iterative approach


# def binary_search(arr, val):

#     # this is the is where the low and high values will be evaluated
#     low = 0
#     high = len(arr)-1


#     while low <= high:
#         #  calculating the mid value
#         mid = low + (
#             (high - low) // 2
#         )  # after every iter the low value will be shifted according to the output
#         if arr[mid] == val:
#             return mid
#         elif val < arr[mid]:
#               high = mid - 1
#         else:
#             low = mid + 1
#     return -1


## Recursive approach
def binary_search_helper(arr, high, low, val):

    mid = low + ((high - low) // 2)  # BODMAS

    if arr[mid] == val:
        return -1
    elif val < arr[mid]:
        return binary_search_helper(arr, mid - 1, low, val)
    else:
        return binary_search_helper(arr, high, mid + 1, val)


def binary_search(arr, val):
    high = len(arr) - 1
    low = 0
    return binary_search_helper(arr, high, low, val)
