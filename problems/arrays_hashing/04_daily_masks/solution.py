def solve(logs, start):
    masks = {}
    for c, day in logs:
        offset = day-start
        if 0 <= offset < 7:
            masks[c] = masks.get(c,0) | (1 << offset)
    return sorted(c for c, mask in masks.items() if mask==127)
