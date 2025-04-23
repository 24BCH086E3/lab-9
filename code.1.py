def count_lower_upper(s):
    return {
        "lowercase": sum(1 for c in s if c.islower()),
        "uppercase": sum(1 for c in s if c.isupper())
    }

print(count_lower_upper("Hello World! This Is Python."))
