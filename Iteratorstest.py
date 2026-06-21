import itertools

# for i in itertools.count(10, 2):   # start=10, step=2
#     if i > 20:
#         break
#     print(i)

# sales =[("apple", 1), ("apple", 2), ("banana", 3)]
# for fruit, quantity in sales:
#     print(fruit, quantity)

data = [("apple", 1), ("apple", 2), ("banana", 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

