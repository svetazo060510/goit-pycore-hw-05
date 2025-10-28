import re
from typing import Callable, Generator
from decimal import Decimal

def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    # Regular expression for searching for real numbers (including integers)
    pattern = r"\b\d+(\.\d+)?\b"
    
    # re.finditer returns iterator
    for match in re.finditer(pattern, text):
        # match.group(0) returns the full match found
        yield Decimal(match.group(0))

def sum_profit(text: str, func: Callable[[str], Generator[Decimal, None, None]]) -> Decimal:
    total = Decimal('0.0')
    
    # Iterate over the generator and sum the numbers.
    for number in func(text):
        total += number
        
    return total

# -- Usage example --
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# -- Additional test with integers --
text_2 = "Нові надходження 500, 700.50 та 20.25."
total_income_2 = sum_profit(text_2, generator_numbers)
print(f"Загальний дохід 2: {total_income_2}")
