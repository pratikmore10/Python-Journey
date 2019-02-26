hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)


def computepay():
    extra_hrs = h-40
    extra_time = r*1.5
    nh = h*r
    o_hrs = 40*r + extra_hrs*extra_time
    if h <= 40:
        return nh
    elif h > 40:
        return o_hrs


print(computepay())

