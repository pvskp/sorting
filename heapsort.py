def parent(i: int) -> int:
    return i // 2


def right(i: int) -> int:
    return 2 * i + 2


def left(i: int) -> int:
    return 2 * i + 1


def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def max_heapify(arr: list[int], n: int, current: int) -> None:
    left_child = left(current)  # indice left_child
    right_child = right(current)  # indice right_child

    if left_child < n and right_child < n:
        print(f"current: {current} left: {left_child} right: {right_child}")
        print(
            f"arr[{current}]: {arr[current]} arr[{left_child}]: {arr[left_child]} arr[{right_child}]: {arr[right_child]}"
        )

    bigger: int = current

    if left_child < n and arr[left_child] > arr[current]:
        bigger = left_child

    if right_child < n and arr[right_child] > arr[current]:
        bigger = right_child

    if bigger != current:
        print(f"swapping index {current} with {bigger}")
        print(f"{arr[current]} <-> {arr[bigger]}")
        swap(arr, current, bigger)
        print(f"current array is {arr}")
        max_heapify(arr, n, bigger)


def build_max_heap(arr):
    n = len(arr)
    # Começa do último nó pai até a raiz (índice 0)
    print(f"last parent: arr[{n//2 - 1}]")
    for i in range(n // 2 - 1, -1, -1):
        print(f"i = {i}")
        max_heapify(arr, n, i)


def main() -> None:
    arr: list[int] = [2, 1, 3, 6, 7, 10, 22]
    print(f"initial array {arr}")
    build_max_heap(arr)
    print(f"final array {arr}")
    ...


if __name__ == "__main__":
    main()
