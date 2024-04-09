# Get only the even or odd index elements of a Python List

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ get all elements with an even index in the list
even = my_list[::2]
print(even)  # 👉️ [0, 2, 4, 6, 8, 10]

# ---------------------------------------------

# ✅ get all elements with an odd index in the list
odd = my_list[1::2]
print(odd)  # 👉️ [1, 3, 5, 7, 9]

# ---------------------------------------------

# ✅ get every second element of the list (starting with the second element)
n = 2
every_second = my_list[n - 1::n]
print(every_second)  # 👉️ [1, 3, 5, 7, 9]

# ---------------------------------------------

# ✅ get every second element of the list (starting at index 2)
every_second = my_list[2::2]
print(every_second)  # 👉️ [2, 4, 6, 8, 10]