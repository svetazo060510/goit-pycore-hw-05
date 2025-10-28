from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    # Створюємо порожній словник cache.
    cache = {}

    def fibonacci(n: int) -> int:
        # Базові випадки ряду Фібоначчі
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Перевірка, чи є значення вже у кеші
        if n in cache:
            return cache[n]  

        # Якщо значення немає у кеші, обчислюємо його рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# -- Приклад використання --
# Отримуємо функцію fibonacci, яка "пам'ятає" свій кеш
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел
# При першому виклику fib(10), вона обчислить і закешує
# fib(1) ... fib(10).
print(f"fib(10) = {fib(10)}")  # Виведе 55

# При виклику fib(15), вона використає вже збережені
# значення від 1 до 10 і обчислить лише fib(11) ... fib(15).
print(f"fib(15) = {fib(15)}")  # Виведе 610

# Цей виклик буде миттєвим, оскільки fib(10) вже є в кеші
print(f"fib(10) = {fib(10)}")  # Виведе 55
