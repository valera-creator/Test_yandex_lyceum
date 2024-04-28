def is_prime(n):
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print("YES" if is_prime(int(input())) else "NO")
