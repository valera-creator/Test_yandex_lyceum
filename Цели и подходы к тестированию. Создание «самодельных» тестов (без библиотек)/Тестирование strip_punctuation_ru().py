from yandex_testing_lesson import strip_punctuation_ru


def test_is_correct_mobile_phone_number_ru():
    test_case = (
        ('много,разной.пунктуации!', 'много разной пунктуации'),
        ('слов с дефисами видимо-невидимо', 'слов с дефисами видимо-невидимо'),
        (',', '',),
        ('avcwsfsafd()', 'avcwsfsafd'),
        ('бред — хрень бред', 'бред хрень бред'),
        ('параша,параша.параша!параша?параша:параша - параша', 'параша параша параша параша параша параша параша')
    )

    for elem in test_case:
        if strip_punctuation_ru(elem[0]) != elem[1]:
            return False
    return True


print("YES" if test_is_correct_mobile_phone_number_ru() else "NO")
