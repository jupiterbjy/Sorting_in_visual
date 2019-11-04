import inspect
from sys import modules

'''
Return list of target, i.e. Class or Function.
'''

def ListTarget(name, target, name_only):
    members = inspect.getmembers(modules[name], target)
    if name_only:
        return [a for a, _ in members]
    
    else:
        return members
    
    
def ListClass(name, name_only = False):
    return ListTarget(name, inspect.isclass, name_only)
    
def ListFunction(name, name_only = False):
    return ListTarget(name, inspect.isfunction, name_only)