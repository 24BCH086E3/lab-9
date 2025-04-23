def average(lst, total=0, count=0):
    if not lst:
        return total / count if count != 0 else 0
    return average(lst[1:], total + lst[0], count + 1)

lst = [10, 20, 30, 40]
print("Average:", average(lst))
