# Test Case array ele -> 1,2.3,4,5,6,7,8,9


def array_rotation_helper(arr, low, high):

    # calculating the mid
    mid = low + (high - low) // 2

    # checking the pivoting point or the rotation point

    # if the pivot point is the next value
    if (
        mid < high and arr[mid + 1] > arr[mid]
    ):  # mid < high is explicitly checking the index area which we are searching
        return mid + 1

    # if pivot point is the mid
    if (
        mid > low and arr[mid] < arr[mid - 1]
    ):  # mid < high is explicitly checking the index area which we are searching
        return mid

    # moving towards the problem or the pivot point
    if arr[mid] < arr[high]:
        return array_rotation_helper(arr, low, mid - 1)

    return array_rotation_helper(arr, mid + 1, high)
