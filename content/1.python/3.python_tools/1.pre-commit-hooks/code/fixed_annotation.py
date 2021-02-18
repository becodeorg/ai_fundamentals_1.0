from typing import Union


def divide(a: int, b: int) -> Union[float, str]:
    if b != 0:
        return float(a / b)
    else:
        return "Can't divide by zero. Please change the value of b."
