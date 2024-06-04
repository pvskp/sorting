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

    bigger: int = current

    if left_child < n and arr[left_child] > arr[bigger]:
        bigger = left_child

    if right_child < n and arr[right_child] > arr[bigger]:
        bigger = right_child

    if bigger != current:
        swap(arr, current, bigger)
        max_heapify(arr, n, bigger)


def build_max_heap(arr):
    n = len(arr)
    # Começa do último nó pai até a raiz (índice 0)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heapsort(arr: list[int]):
    build_max_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)  # troca atual com maior elemento
        max_heapify(arr, i, 0)


def main() -> None:
    arr = [10, 2222, 56, 32, 2, 5, 1, 6, 8, 8, 1, 4]
    # build_max_heap(arr)
    heapsort(arr)
    print(f"sorted array: {arr}")


if __name__ == "__main__":
    main()
