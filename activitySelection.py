from ActivityModel import Activity
from PrintUtils import printActivity


def activitySelection(arr: list[Activity]):
    # Create an empty array to store the result
    result = []

    # Sort the array based on the second element of the tuple
    arr.sort(key=lambda act: act.end)

    # Add the first element to the result array
    i = 0
    result.append(arr[i])

    # Iterate through the array and
    # add the element to the result array if the start time is greater than
    # the end time of the previous element
    for j in range(1, len(arr)):
        if arr[j].start >= arr[i].end:
            result.append(arr[j])
            i = j

    return result
