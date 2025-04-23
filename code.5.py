def ispangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))
