"""Hey Jonh, I hope you enjoyed your vacations. There is some issues with this code. Welcome back!"""
import subprocess


def divide(a: int, b: int) -> Union[float, str]:
    if b != 0:
        return float(a / b)
    else:
        return "Can't divide by zero. Please change the value of b."


def addition(a: int, b: int) -> int:
    result = a + b
    return f"result is {str(result)}"


def just_another_function(a: int) -> float:
    return a * math.pi
