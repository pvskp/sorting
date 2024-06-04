def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr: list[int], start: int, end: int) -> int:
    pivot_index = end  # uses arr[end] as pivot
    pivot = arr[pivot_index]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, pivot_index)

    return i + 1


def quicksort(arr: list[int], start: int, end: int):
    if start < end:
        q = partition(arr, start, end)
        quicksort(arr, start, q - 1)
        quicksort(arr, q + 1, end)


def main() -> None:
    arr = [10, 2222, 56, 32, 2, 5, 1, 6, 8, 8, 1, 4]
    quicksort(arr, 0, len(arr) - 1)
    print(f"sorted arr: {arr}")


if __name__ == "__main__":
    main()
