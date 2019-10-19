import threading as th

import Bubble
import visualizing as vl
import Source_array as sa
import Sorting_loader


# Don't put () on target, or it will return result of that function!
# TODO: decide whether to pass copy of class instance via copy module

t = sa.Source(30)

th1 = td.Thread(target = Sorting_loader, args = (t))
th_visual = td.Thread(target = vl.Main, args = ())


