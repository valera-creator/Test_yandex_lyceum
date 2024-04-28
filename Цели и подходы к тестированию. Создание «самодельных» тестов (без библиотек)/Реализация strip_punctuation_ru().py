def strip_punctuation_ru(s):
    exclude = "'.,;:?!"
    s = s.split()
    for elem in range(len(s)):
        if len(s[elem]) == 1 and s[elem] == "-":
            s[elem] = ""
        for book in range(len(s[elem])):
            s[elem] = list(s[elem])
            if s[elem][book] in exclude:
                s[elem][book] = " "
        s[elem] = "".join(s[elem])
    return " ".join(" ".join(s).split())