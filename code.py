from typing import List

def fibbomnachi(n:int):
    #  """Рекурсия"""
    if n in {0, 1}:
        return n
    result = fibbomnachi(n - 1) + fibbomnachi(n - 2)
    return result


# print(
#     [fibbomnachi(n) for n in range(15)]
# )

a = {n: fibbomnachi(n) for n in range(15)}
print('\n'.join("{}: {}".format(k, v) for k, v in a.items()))

# Expanded:
for key, value in a.items():
    print("{}: {}".format(key, value))
