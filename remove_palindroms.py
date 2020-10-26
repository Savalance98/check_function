def remove_palindroms(spells):
    i = 0
    while i < len(spells):
        p = spells[i].replace(' ', '').lower()
        if p == p[::-1]:
            spells.pop(i)
        else:
            i += 1
    return spells
