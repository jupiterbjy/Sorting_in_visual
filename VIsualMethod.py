
def inline(access, write, color_func_map, array, pad):
    print(*(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}")
