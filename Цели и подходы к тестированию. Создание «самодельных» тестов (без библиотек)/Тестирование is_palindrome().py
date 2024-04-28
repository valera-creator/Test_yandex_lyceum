from yandex_testing_lesson import is_palindrome


def test_palindrom():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        ('aba', True),
        ('abc', False),
        ('a', True))

    for elem in test_data:
        if is_palindrome(elem[0]) != elem[1]:
            return False
    return True


print("YES" if test_palindrom() else "NO")
