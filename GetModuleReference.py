from sys import modules
from inspect import getmembers, isclass, isfunction
from types import ModuleType
from typing import List, Tuple, Any


def ListTarget(module_name: (str, ModuleType), target, blacklist: set, return_dict, local_only):

    if blacklist is None:
        blacklist = set()

    try:
        target_module = modules[module_name]
    except KeyError:
        if isinstance(module_name, ModuleType):
            target_module = module_name
        else:
            raise

    members = getmembers(target_module, target)

    def filter_gen(source: List[Tuple[str, Any]]):
        if local_only:
            source = [(name, ref) for name, ref in source if modules[ref.__module__] is target_module]

        for name, ref in source:
            if name not in blacklist and not name.startswith("_"):
                yield name, ref

    if return_dict:
        return {name: ref for name, ref in filter_gen(members)}
    else:
        return tuple(name for name, _ in filter_gen(members))


def ListClass(name, blacklist: set = None, return_dict=False, local_only=True):
    return ListTarget(name, isclass, blacklist, return_dict, local_only)


def ListFunction(name, blacklist: set = None, return_dict=False, local_only=True):
    return ListTarget(name, isfunction, blacklist, return_dict, local_only)
