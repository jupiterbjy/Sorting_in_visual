import asyncio
import random
import re
from typing import Tuple

import PureSorts
import GetModuleReference
from itertools import cycle
from MutableWrapper import ArrayWrap
from collections.abc import MutableSequence
from VisualMethod import OutputMethods, ANSIWrap


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


def get_size() -> tuple:
    raw_input = input("Set single or multiple number of items to sort: ")

    try:
        return tuple(map(int, re.split(r"(?:!+|-+| +|/+|\.+)", raw_input)))
    except ValueError:
        return get_size()
    finally:
        ANSIWrap.clear()
        # I don't expect someone `mistakenly` call this function up to recursion limit.


def get_delay() -> Tuple[float, bool]:
    delay = 0.003

    while True:
        raw_input = input("Float delay between each frame(default 0.003sec): ")

        if not raw_input:
            break

        try:
            delay = float(raw_input)
        except ValueError:
            continue
        break

    while True:
        raw_input = input("Require enter press on every frame?(y/n - default n): ")
        if not raw_input:
            return delay, False

        if set(raw_input) & set("yY"):
            return delay, True

        if set(raw_input) & set("nN"):
            return delay, False


def select_visualize_method() -> list:

    visual_list = GetModuleReference.ListFunction(
        OutputMethods, blacklist={"create_horizontal"}
    )
    show_list(visual_list)

    # get visual method
    raw_input = input("Enter multiple visualizing method index: ")
    try:
        selected_list = [
            getattr(OutputMethods, visual_list[i])
            for i in map(int, re.split(r"(?:!+|-+| +|/+|\.+)", raw_input))
        ]

    except IndexError:
        print("Index provided out of range, try again.")
        return select_visualize_method()

    except ValueError:
        print("Wrong index provided, try again.")
        return select_visualize_method()
    else:
        return selected_list
    finally:
        ANSIWrap.clear()


def select_sorts_list() -> list:
    ANSIWrap.clear()

    # show list of sorts implemented
    sort_list = PureSorts.__all__
    show_list(sort_list)

    # get list of sorts to play
    raw_list = input("Enter multiple index of sorts to play: ")
    try:
        selected_list = [
            getattr(PureSorts, sort_list[i])
            for i in map(int, re.split(r"(?:!+|-+| +|/+|\.+)", raw_list))
        ]

    except IndexError:
        print("Index provided out of range, try again.")
        return select_sorts_list()

    except ValueError:
        print("Wrong index provided, try again.")
        return select_sorts_list()
    else:
        return selected_list
    finally:
        ANSIWrap.clear()


async def visual_task(
    q: asyncio.Queue,
    arr_reference: ArrayWrap,
    visualize,
    sort_name: str,
    delay=0.003,
    wait_input=True,
):
    """
    Task dealing with output handling.
    :param arr_reference: Pass reference of currently sorted array.
    :param visualize: Function to draw
    :param sort_name: Name of sorting algorithm in-run.
    :param wait_input:
    :param delay:
    :param q:
    """

    largest_digit = len(str(max(arr_reference)))
    ANSIWrap.clear()

    while True:
        try:
            access, write, color_func_map, frame = await q.get()
        except TypeError:
            visualize(*arr_reference.mark_all_sorted(), largest_digit, sort_name)
            break
        else:
            visualize(access, write, color_func_map, frame, largest_digit, sort_name)

        await asyncio.sleep(delay)
        if wait_input:
            input("Press Enter to continue: ")


async def run_sort(sort_func, arr: ArrayWrap):
    sort_func(arr)
    await arr.queue.put(None)  # intentionally raise error in visual_task


async def sort_main(sort_list, visualizer, testcases, delay, require_input):

    for idx, (sort, visual, test) in enumerate(
        zip(sort_list, cycle(visualizer), cycle(testcases))
    ):
        steps_queue = asyncio.Queue()

        list_object = ArrayWrap(test, steps_queue)

        visual = asyncio.create_task(
            visual_task(steps_queue, list_object, visual, sort.__name__, delay, require_input)
        )
        sort_task = asyncio.create_task(run_sort(sort, list_object))

        await sort_task
        await visual
        print(f"\n{idx + 1}/{len(sort_list)} Completed.")
        await asyncio.sleep(1.5)


def main_loop():

    while True:
        sort_list = select_sorts_list()
        print(f"Selected: {' '.join(i.__name__ for i in sort_list)}")
        testcase_list = map(generate_test, get_size())
        visual_list = select_visualize_method()
        delay, require_input = get_delay()

        asyncio.run(sort_main(sort_list, visual_list, testcase_list, delay, require_input))

        break


if __name__ == "__main__":
    main_loop()

"""
1 9 3 19 17 6 12 7 5 4 10 8
20 20 20 30 20 20 60 60 40 60 40 60
0 1 1 0 0 0 0 0 0 2 0 0
"""
