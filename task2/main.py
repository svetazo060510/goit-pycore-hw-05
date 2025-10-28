import re
from typing import Callable, Generator
from decimal import Decimal

def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    # Регулярний вираз для пошуку дійсних чисел (включно з цілими)
    pattern = r"\b\d+(\.\d+)?\b"
    
    # re.finditer повертає ітератор
    for match in re.finditer(pattern, text):
        # match.group(0) повертає повний знайдений збіг (напр., "1000.01")
        # Ми створюємо Decimal з рядка для збереження повної точності
        yield Decimal(match.group(0))

def sum_profit(text: str, func: Callable[[str], Generator[Decimal, None, None]]) -> Decimal:
    # Ініціалізуємо total як Decimal '0.0' для точних розрахунків
    total = Decimal('0.0')
    
    # Викликаємо передану функцію 'func' з текстом, що повертає нам генератор.
    # Ітеруємо по генератору і підсумовуємо числа.
    for number in func(text):
        total += number
        
    return total

# -- Приклад використання --
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# -- Додатковий тест з цілими числами --
text_2 = "Нові надходження 100, 200.50 та 50.25."
total_income_2 = sum_profit(text_2, generator_numbers)
print(f"Загальний дохід 2: {total_income_2}")
