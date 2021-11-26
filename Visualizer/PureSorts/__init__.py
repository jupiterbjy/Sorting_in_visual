from .ExchangeSorts import *
from .SelectionSorts import *
from .InsertionSorts import *
from .MergeSorts import *
from .Temporary import *

import GetModuleReference

__all__ = GetModuleReference.ListFunction(__name__, local_only=False)
print(f"[PureSorts] Loaded {len(__all__)} of sorts.")
