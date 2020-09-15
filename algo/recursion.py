
def factorial(n):
    if n < 2:
        return 1
    return factorial(n-1)*n


def binary_search(data, target, low=None, high=None):
    """
    1 2 3 4 5 6

    1 2 3
      2 3
    """
    low = low if low is not None else 0
    high = high if high is not None else len(data) - 1
    if low > high:
        return None
    mid = (high + low) // 2
    if data[mid] == target:
        return mid
    if target < data[mid]:
        return binary_search(data, target, low, mid-1)
    return binary_search(data, target, mid+1, high)


def binary_sum(data, low=None, high=None):
    low = low if low is not None else 0
    high = high if high is not None else len(data)
    if low >= high:
        return 0
    if low == high-1:
        return data[low]
    mid = (high+low) // 2
    return binary_sum(data, low, mid) + binary_sum(data, mid, high)
