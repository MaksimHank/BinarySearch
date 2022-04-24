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

print({n: fibbomnachi(n) for n in range(15)})