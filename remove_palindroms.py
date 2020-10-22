def remove_palindroms(spells):
    t = ''
    i = 0
    while i < len(spells):
        p = spells[i].split()
        p = ''.join(p)
        for j in range(len(p) - 1, - 1, - 1):
            t += p[j].lower()
        if str(p).lower() == t:
            spells.pop(i)
        else:
            i += 1
        t = ''
    return spells
