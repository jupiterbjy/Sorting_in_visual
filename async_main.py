import asyncio
import random
import re
import Sorting_algorithms_pure
import VisualMethod
import GetModuleReference
from MutableWrapper import ArrayWrap
from collections.abc import MutableSequence


def get_size():
    size = input("Set number of items to sort: ")

    try:
        return int(size)
    except ValueError:
        return get_size()
        # I don't expect someone `mistakenly` call this function up to recursion limit.


def generate_test(n: int):
    return shuffle([i for i in range(1, n + 1)])


def shuffle(arr: MutableSequence):
    # using Fisher-Yates shuffles algorithm.

    length = len(arr)

    for i in range(length - 2):
        j = random.randint(0, length - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def show_list(items):
    digit = len(str(len(items)))

    for idx, item in enumerate(items):
        print(f"{idx:{digit}} {item}")


def select_visualize_method():
    visual_list = GetModuleReference.ListFunction(VisualMethod)
    show_list(visual_list)

    # get visual method
    raw_input = input("Enter visualizing method index: ")
    try:
        selected = getattr(VisualMethod, visual_list[int(raw_input)])
    except ValueError:
        print("Wrong index provided, try again.")
        return select_visualize_method()

    return selected


def select_sorts_list() -> list:
    # show list of sorts implemented
    sort_list = GetModuleReference.ListFunction(Sorting_algorithms_pure)
    show_list(sort_list)

    # get list of sorts to play
    raw_list = input("Enter multiple index of sorts to play: ")
    try:
        selected_list = [getattr(Sorting_algorithms_pure, sort_list[i])
                         for i in map(int, re.split(r"(?:!+|-+| +|/+|\.+)", raw_list))]

    except IndexError:
        print("Index provided out of range, try again.")
        return select_sorts_list()

    except ValueError:
        print("Wrong index provided, try again.")
        return select_sorts_list()

    else:
        return selected_list


async def visual_task(q: asyncio.Queue, arr_reference: MutableSequence, visualize):
    """
    Task dealing with output formatting.
    :param q:
    :param arr_reference: Pass reference of currently sorted array.
    :param visualize: Function to draw
    """

    largest_digit = len(str(max(arr_reference)))

    while True:

        try:
            access, write, color_func_map, frame = await q.get()
        except TypeError:
            break
        else:
            visualize(access, write, color_func_map, frame, largest_digit)

        await asyncio.sleep(0.1)


async def run_sort(sort_func, arr: ArrayWrap):
    sort_func(arr)
    await arr.queue.put(None)  # end_val


async def sort_main(sort_list, test: MutableSequence, visualizer):
    for sort_type in sort_list:
        print(sort_type.__name__)
        steps_queue = asyncio.Queue()
        list_object = ArrayWrap(test, steps_queue)

        visual = asyncio.create_task(visual_task(steps_queue, list_object, visualizer))
        sort_task = asyncio.create_task(run_sort(sort_type, list_object))

        await sort_task
        await visual


def main_loop():

    while True:
        testcase = generate_test(get_size())
        sort_list = select_sorts_list()
        visualizing_method = select_visualize_method()

        asyncio.run(sort_main(sort_list, testcase, visualizing_method))

        break


if __name__ == '__main__':
    main_loop()
