from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test_is_correct_mobile_phone_number_ru():
    test_case = (
        ('123(45677', False),
        ("211111111111", False),
        ("8(666)1234567", True),
        ("+7 612 123 4567", True),
        ("+7-981-123-45-67", True),
        ("+7123(456)68-90", False),
        ('avbbqsdgsdadgs', False)
    )

    for elem in test_case:
        if is_correct_mobile_phone_number_ru(elem[0]) != elem[1]:
            return False
    return True


print("YES" if test_is_correct_mobile_phone_number_ru() else "NO")
