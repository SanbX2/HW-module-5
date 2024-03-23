from typing import Callable

import re

def generator_numbers(text: str):
    floats = re.findall(r'\b\d+\.\d+\b', text)

    for number in floats:
        yield float(number)

def sum_profit(text: str, func: Callable):
    total = 0
    for num in func(text):
        total += num
        return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
gen = generator_numbers(text)
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")