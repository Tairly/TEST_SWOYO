def prime_numbers(low, high):
    # Приведение нижней границы к 2
    if low < 2:
        low = 2

    # Проверка верхней границы
    if high < 2 or high < low:
        return []

    # Cписок, состоящий из логических значений
    is_prime = [True] * (high + 1)

    # Цикл перебирает все числа от 2 до квадратного корня из h (по св-ву пр. чисел)
    for i in range(2, int(high ** 0.5) + 1):
        if is_prime[i]:
            start = max(i * i, ((low + i - 1) // i) * i)
            for i in range(start, high + 1, i):
                is_prime[i] = False

    primes = [i for i in range(low, high + 1) if is_prime[i]]
    return primes


# Реализация
low = 10
high = 2500
print(prime_numbers(low, high))
