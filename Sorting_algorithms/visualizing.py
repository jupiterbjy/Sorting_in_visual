import Source_array as arr

# TODO: actually output something and sync array sampling timing via
# 'signal' bool var in Source_array's 'Source' class.

def Output():
    # doing vertical for now
    for i in arr.array:
        print("#" * i)
        
    print(arr.compare, arr.access)

def Main(arr_class):
    while True:
        if arr_class.signal:
            # start sampling, I only got 1 and half minutes. committing!
        time.sleep(arr.delay)

        Output()
    