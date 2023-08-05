def zigzag(s: str, ms: int) -> str:
    if ms == 1 or len(s) <= ms:
        return s

    rows = [''] * ms
    index, step = 0, 1

    for c in s:
        rows[index] += c

        if index == 0:
            step = 1
        elif index == ms - 1:
            step = -1

        index += step

    return ''.join(rows)

s = "paypalisawesome"
print(zigzag(s, 3))
