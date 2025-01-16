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
            totalCost += calculate_A_cost(sku_counts)
        elif k == 'B':
            totalCost += calculate_B_cost(sku_counts)
        else:
            totalCost += v * sku_map[k]
    return totalCost

def calculate_A_cost(sku_counts):
    cost = 0
    while sku_counts['A'] >= 5:
        cost += 200
        sku_counts['A'] -= 5
    while sku_counts['A'] >= 3:
        cost += 130
        sku_counts['A'] -= 3
    cost += sku_counts['A'] * 50
    return cost


def calculate_B_cost(sku_counts):
    number_of_free_Bs = sku_counts['E'] // 2
    sku_counts['B'] -= number_of_free_Bs
    number_of
    return (sku_counts['B'] % 2) * sku_map['B'] + (sku_counts['B']  // 2) * 45

