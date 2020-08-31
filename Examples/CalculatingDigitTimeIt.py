from timeit import timeit


def digit_loop(n):
    p = 1
    while n := n//10:
        p += 1
    return p


def digit_str_converting(n):
    return len(str(n))


print(timeit(lambda: digit_loop(10000000)))
print(timeit(lambda: digit_str_converting(10000000)))

'''
0.5678788
0.270292

HOW?????????  Gonna ask this on SO
'''
