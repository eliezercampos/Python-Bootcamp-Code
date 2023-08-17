# canasta = {"manzana", "pera", "manzana", "naranja", "platano", "naranja"}

# print(canasta)

# print("manzana" in canasta)

# print("melon" in canasta)

# vocales = ["a", "e", "i", "o", "u", "a"]

# print(vocales)

# vocales = list(set(vocales))

# print(vocales)

# vocales1 = {"a", "e", "i", "o", "u", "a"}

# vocales2 = {"e", "i", "o"}

# print(vocales2.issubset(vocales1))

vocales1 = {"a", "e", "i", "o", "u"}

vocales2 = {"A", "E", "I", "O", "U"}

print(vocales1 - vocales2)

print(vocales1 | vocales2)

print(vocales1 & vocales2)

print(vocales1 ^ vocales2)