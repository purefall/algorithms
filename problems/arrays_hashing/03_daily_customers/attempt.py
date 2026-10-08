"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""

LOYALITY_DURATION = 6


def solve_with_sum(logs, start) -> list[str]:
    seen_customers = {}
    loyal_customer = set()
    # Due to Day 0
    shifted_start = start + 1
    loyality_end_date = shifted_start + LOYALITY_DURATION
    loyality_sum = (
        loyality_end_date * (loyality_end_date + 1) / 2
        - shifted_start * (shifted_start - 1) / 2
    )
    for ii, log in enumerate(logs):
        cur_customer, cur_date = log[0], log[1]

        cur_customer_relative_visits = seen_customers.get(cur_customer, set())
        if cur_date + 1 >= shifted_start and cur_date + 1 <= loyality_end_date:
            cur_customer_relative_visits.add(cur_date + 1)
            seen_customers[cur_customer] = cur_customer_relative_visits

        if sum(cur_customer_relative_visits) == loyality_sum:
            loyal_customer.add(cur_customer)

    return sorted(loyal_customer)


def solve(logs, start):

    day = {}

    for ii, log in enumerate(logs):
        cur_customer, cur_date = log[0], log[1]
        if start <= cur_date <= start + LOYALITY_DURATION:
            day.setdefault(cur_customer, set()).add(cur_date)

    return sorted(
        [
            customer
            for customer, visited_dates in day.items()
            if len(visited_dates) == LOYALITY_DURATION + 1
        ]
    )


full = lambda c, s: [(c, d) for d in range(s, s + 7)]

# Given example
assert solve(
    [("a", 0), ("a", 1), ("a", 2), ("a", 3), ("a", 4), ("a", 5), ("a", 6), ("b", 0)], 0
) == ["a"]

# Output must be sorted, even if input order isn't
assert solve(full("c", 0) + full("a", 0) + full("b", 0), 0) == ["a", "b", "c"]

# Duplicate visits don't count as extra days: 'a' has 7 entries but misses day 6
assert solve([("a", d) for d in [0, 0, 1, 2, 3, 4, 5]], 0) == []

# Days outside the window are ignored: 'a' fills the window, extras don't hurt
assert solve(full("a", 0) + [("a", -1), ("a", 7), ("a", 100)], 0) == ["a"]

# Days outside the window don't help: 'b' has 7 days, but they're 1..7, not 0..6
assert solve(full("b", 1), 0) == []

# Non-zero start
assert solve(full("x", 10) + full("y", 9), 10) == ["x"]

# Empty input
assert solve([], 0) == []

print("all passed")
