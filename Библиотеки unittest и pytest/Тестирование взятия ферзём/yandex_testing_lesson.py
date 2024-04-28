def is_under_queen_attack(position, queen_position):
    if type(position) is not str:
        raise TypeError

    if not (len(position) == 2 and position[0] in 'abcdefgh' and position[1] in '12345678'):
        raise ValueError

    if type(queen_position) is not str:
        raise TypeError

    if not (len(queen_position) == 2 and queen_position[0] in 'abcdefgh' and queen_position[1] in '12345678'):
        raise ValueError

    f2, s2 = int(position[1]), int(queen_position[1])

    if not (1 <= f2 <= 8 and 1 <= s2 <= 8):
        raise ValueError

    translat_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    f1, s1 = translat_to_num[position[0]], translat_to_num[queen_position[0]]

    if position[0] == queen_position[0] or position[1] == queen_position[1]:
        return True

    return abs(f1 - s1) == abs(f2 - s2)
