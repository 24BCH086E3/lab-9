def sanitize(lst):
    if not lst:
        return []
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize(lst[1:])

lst = [-3, 4, -1, 7, -2]
print("Sanitized list:", sanitize(lst))
