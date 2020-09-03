import asyncio
import random
import re
import Sorting_algorithms_pure
from new_support import ArrayWrap
from collections.abc import MutableSequence


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
        selected_list = [getattr(Sorting_algorithms_pure, sort_list[i])
                         for i in map(int, re.split(r"(?:!+|-+| +|/+|\.+)", raw_list))]

    except IndexError:
        print("Index provided out of range, try again.")
        return get_sorts_list()

    except ValueError:
        print("Wrong index provided, try again.")
        return get_sorts_list()

    else:
        return selected_list


async def visual_task(q: asyncio.Queue, pad: int):
    """
    Task dealing with output formatting.
    :param q:
    :param pad: padding size of each int.
    """

    while True:
        try:
            access, write, color_func_map, frame = await q.get()
        except TypeError:
            break
        else:
            print(*(f(f"{i:{pad}}") for f, i in zip(color_func_map, frame)), f"|{access} {write}")

        await asyncio.sleep(0.05)


async def run_sort(sort_func, arr: ArrayWrap):
    sort_func(arr)
    await arr.queue.put(10)  # end_val
    print()


async def sort_main(sort_list, test: MutableSequence):
    for sort_type in sort_list:
        print(sort_type.__name__)
        steps_queue = asyncio.Queue()
        list_object = ArrayWrap(test, steps_queue)
        largest_digit = len(str(max(list_object)))

        visual = asyncio.create_task(visual_task(steps_queue, largest_digit))
        sort_task = asyncio.create_task(run_sort(sort_type, list_object))

        await sort_task
        await visual


def main_loop():

    while True:
        testcase = generate_test(get_size())
        sort_list = get_sorts_list()

        asyncio.run(sort_main(sort_list, testcase))

        break


if __name__ == '__main__':
    main_loop()
