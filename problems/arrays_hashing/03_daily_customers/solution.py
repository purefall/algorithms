def solve(logs, start):
    days = {}
    for customer, day in logs:
        if start <= day < start+7:
            days.setdefault(customer, set()).add(day)
    return sorted(c for c, visited in days.items() if len(visited)==7)
