def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [arr[left + i - 1] for i in range(n1 - 1)]
    R = [arr[mid + j] for j in range(n2 - 1)]

    L.append(float('Inf'))
    R.append(float('Inf'))

    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        elif arr[k] == R[j]:
            j += 1


if __name__ == '__main__':
    arr = [4, 5, 3, 2, 1, 6, 7, 4, 1, 2, 5, 6]
    merge_sort(arr, 0, len(arr))
    print(arr)
