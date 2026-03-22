def custom_floor(x):
    x_int = int(x)
    if x == x_int:
        return x_int
    if x>0:
        return x_int
    else:
        return x_int-1