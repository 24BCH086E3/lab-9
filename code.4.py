def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print(sum_avg([85, 90, 78, 92, 88]))
