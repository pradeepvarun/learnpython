a = {"abc", "def", "xyz", "gih" }
b = {"def", "cde"}

# Minus
print(a.difference(b))  # Display element that is part of "a" but not part of "b"
print(b.difference(a))  # Display element that is part of "b" but not part of "a"

result = a.difference(b)
print(result)
result = b.difference(a)
print(result)


# Union of both set
print(a.union(b))
print(b.union(a))

# intersection
print(a.intersection(b))
print(b.intersection(a))
