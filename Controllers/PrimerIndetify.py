from sympy import isprime
from threading import Thread

CAPTURE: list = []


def choiceNumber(number: str) -> int:
    simbols = ['+', ',', '-', ':', '@', '*', '/']
    try:
        if number.strip() not in simbols: eval(f"{number} + 1")
    except Exception: return 0
    else:
        try: int(number)
        except Exception: return 0
        else:
            if isprime(int(number)): return int(number)
            else: return 0


def capture(*args) -> list[dict]:
    for itens in args:
        for k, v in args:
            CAPTURE.append([k, v])
    return CAPTURE


if __name__ == '__main__':
    print(choiceNumber('321509'))
