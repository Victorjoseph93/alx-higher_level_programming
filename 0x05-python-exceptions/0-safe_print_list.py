#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0

    for i in range(0, x):
        print(f"{my_list[i]", end="")
            i += 1
        except indexError:
            pass
    finally:
        print()
    return i
