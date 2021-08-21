import typing as t


def add(x: float, y: t.Optional[float] = 2) -> [float, int]:
    return x + y


def product(x, y=2):
    return x * y


print(add(2, 3))
print(type(add(2, 3)))
