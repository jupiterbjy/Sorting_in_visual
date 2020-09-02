import asyncio
import random
import re
import Sorting_algorithms_pure
from new_support import ArrayWrap
from collections.abc import Sequence, MutableSequence


def get_size():
    size = input("Set number of items to sort: ")

    try:
        return int(size)
    except ValueError:
        return get_size()
        # I don't expect someone `mistakenly` call this function up to recursion limit.


def select_visualize_method():
    pass


def generate_test(n: int):
    return shuffle([i for i in range(1, n + 1)])


def shuffle(arr: MutableSequence):
    # using Fisher-Yates shuffles algorithm.

    length = len(arr)

    for i in range(length - 2):
        j = random.randint(0, length - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def get_sorts_list() -> list:
    # show list of sorts implemented
    sort_list = sorted(Sorting_algorithms_pure.__all__)
    digit = len(str(len(sort_list)))

    for idx, sort in enumerate(sort_list):
        print(f"{idx:{digit}} {sort}")

    # get list of sorts to play
    raw_list = input("Enter multiple index of sorts to play: ")
    try:
        selected_list = [sort_list[i] for i in map(int, re.split(r"(!+|-+| +|/+|\.+)", raw_list))]

    except IndexError:
        print("Index provided out of range, try again.")
        return get_sorts_list()

    except ValueError:
        print("Wrong index provided, try again.")
        return get_sorts_list()

    else:
        return selected_list


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


async def run_sort(arr: ArrayWrap):
    Sorting_algorithms_pure.Heap(arr)
    # new_sort_pure.Radix_LSD_Base2(arr)
    await arr.queue.put(10)  # end_val


async def sort_main(test: MutableSequence):
    steps_queue = asyncio.Queue()
    list_object = ArrayWrap(test, steps_queue)

    visual = asyncio.create_task(visual_task(steps_queue))
    sort_task = asyncio.create_task(run_sort(list_object))

    await sort_task
    await visual



def main_loop():

    while True:
        testcase = generate_test(get_size())
        sort_list = []

        asyncio.run(sort_main(testcase))


if __name__ == '__main__':
    main_loop()
