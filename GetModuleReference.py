from sys import modules
from inspect import getmembers, isclass, isfunction
from types import ModuleType


def ListTarget(module_name: (str, ModuleType), target, blacklist: set, return_dict):

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

    filtered = [(name, ref) for name, ref in members
                if name not in blacklist
                and not name.startswith('_')
                and module_name is modules[ref.__module__]]

    return {name: ref for name, ref in filtered} if return_dict else tuple(name for name, _ in filtered)


def ListClass(name, blacklist: set = None, return_dict=False):
    return ListTarget(name, isclass, blacklist, return_dict)


def ListFunction(name, blacklist: set = None, return_dict=False):
    return ListTarget(name, isfunction, blacklist, return_dict)
