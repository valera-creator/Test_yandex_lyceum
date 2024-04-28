def count_chars(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    dict_counts = {}
    for elem in set(s):
        dict_counts[elem] = s.count(elem)

    return dict_counts


print(count_chars())
