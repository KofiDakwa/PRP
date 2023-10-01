import math
def ph_finder(C):
    ph = math.log(10,C)
    if ph >= 10:
        return "basic"
    else:
        return "acidic"

print(ph_finder(10))