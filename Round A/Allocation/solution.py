def get_int_input():
    return list(map(int, input().split()))


n_tests = int(input())


def get_max_n_houses(prices, budget):
    prices.sort()
    cost = 0
    n_houses = 0
    for price in prices:
        new_cost = cost + price
        if new_cost > budget:
            break
        cost = new_cost
        n_houses += 1
    return n_houses


n_houses = []
budgets = []
price_lists = []
for i in range(n_tests):
    houses, budget = get_int_input()
    n_houses.append(houses)
    budgets.append(budget)
    price_lists.append(get_int_input())

for i in range(n_tests):
    max_count = get_max_n_houses(price_lists[i], budgets[i])
    print('Case #{}: {}'.format(i+1, max_count))
