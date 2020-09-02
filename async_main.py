import asyncio
import random
import Sorting_algorithms_pure
from new_support import ArrayWrap
from collections.abc import Sequence, MutableSequence


def set_size():
    pass


def select_visualize_method():
    pass


def select_algo():
    pass


async def visual_task(q: asyncio.Queue):
    # first developing one-line mode
    # TODO: add variable digit padding calculation

    padding = "{0:2}"

    while True:
        frame = await q.get()
        try:
            print(*frame)
        except TypeError:
            break

        await asyncio.sleep(0.05)


def shuffle(arr: MutableSequence):
    length = len(arr)

    for i in range(length - 2):
        j = random.randint(0, length - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


async def run_sort(arr: ArrayWrap):
    Sorting_algorithms_pure.Heap(arr)
    # new_sort_pure.Radix_LSD_Base2(arr)
    await arr.queue.put(10)  # end_val


def generate_test(n: int) -> Sequence:
    return shuffle([i for i in range(1, n + 1)])


async def main():
    steps_queue = asyncio.Queue()
    list_object = ArrayWrap(generate_test(20), steps_queue)

    visual = asyncio.create_task(visual_task(steps_queue))
    sort_task = asyncio.create_task(run_sort(list_object))

    await sort_task
    await visual


if __name__ == '__main__':
    asyncio.run(main())
