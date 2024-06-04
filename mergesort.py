def mergesort(arr: list[int], start: int, end: int) -> None:
    if (end - start) > 1:
        mid = (end + start) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr: list[int], start: int, mid: int, end: int) -> None:
    left = []
    right = []

    # creates left list
    for i in range(start, mid):
        left.append(arr[i])

    # creates right list
    for i in range(mid, end):
        right.append(arr[i])

    top_left = 0
    top_right = 0

    for k in range(start, end):
        if top_left >= len(left):
            arr[k] = right[top_right]
            top_right += 1

        elif top_right >= len(right):
            arr[k] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            arr[k] = left[top_left]
            top_left += 1
        else:
            arr[k] = right[top_right]
            top_right += 1


def main() -> None:
    arr = [10, 2222, 56, 32, 2, 5, 1, 6, 8, 8, 1, 4]
    mergesort(arr, 0, len(arr))
    print(f"sorted arr: {arr}")


if __name__ == "__main__":
    main()
