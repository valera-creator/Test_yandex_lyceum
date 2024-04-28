from yandex_testing_lesson import is_prime


def test_is_prime():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False))
    for elem in test_data:
        if is_prime(elem[0]) != elem[1]:
            return False
    return True


print("YES" if test_is_prime() else "NO")
