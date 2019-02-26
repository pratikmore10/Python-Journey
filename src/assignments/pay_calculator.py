
hrs = float(input("Enter Hours: "))
hrs_normal = float(40)
extra_hrs = hrs - hrs_normal
rate = float(input("Enter Rate: "))
extra_time = rate * 1.5
if hrs <= 40:
    print(hrs * rate)
elif hrs > 40:
    print(hrs_normal * rate + extra_hrs*extra_time)
