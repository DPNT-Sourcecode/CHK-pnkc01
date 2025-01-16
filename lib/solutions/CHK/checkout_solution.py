from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

sku_map = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

def checkout(skus):
    sku_counts = defaultdict(int)
    totalCost = 0
    for c in skus:
        if c not in sku_map:
            return -1
        sku_counts[c] += 1

    for k, v in sku_counts.items():
        if k == 'A':
            totalCost += calculate_A_cost(sku_counts['A'])
        elif k == 'B':
            totalCost += calculate_B_cost(sku_counts['B'], sku_counts['E'])
        else:
            totalCost += v * sku_map[k]
    return totalCost

def calculate_A_cost(count_A):
    cost = 0
    while count_A >= 5:
        cost += 200
        count_A -= 5
    while count_A >= 3:
        cost += 130
        count_A -= 3
    cost += count_A * 50
    return cost


def calculate_B_cost(count_B, count_E):
    number_of_paid_Bs = count_B - count_E // 2
    return (number_of_paid_Bs % 2) * number_of_paid_Bs + (number_of_paid_Bs // 2) * 45

