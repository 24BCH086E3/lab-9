def convert(s):
    words = s.split()
    unique_sorted = sorted(set(words))
    return ' '.join(unique_sorted)

print(convert("apple banana apple mango banana orange"))
