from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

sku_map = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
}

def checkout(skus):
    sku_counts = defaultdict(int)
    totalCost = 0
    for c in skus:
        if c not in sku_map:
            return -1
        sku_counts[c] += 1

    if 'A' in sku_counts:
        totalCost += calculate_A_cost(sku_counts['A'])
        del sku_counts['A']
    if 'B' in sku_counts:
        totalCost += calculate_B_cost(sku_counts['B'], sku_counts['E'])
        del sku_counts['B']
    if 'F' in sku_counts:
        totalCost += calculate_F_cost(sku_counts['F'])
        del sku_counts['F']

    for k, v in sku_counts.items():
            totalCost += v * sku_map[k]
    return totalCost

def calculate_A_cost(count):
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
    return (number_of_paid_Bs % 2) * 30 + (number_of_paid_Bs // 2) * 45

def calculate_F_cost(count_F):
    cost = 0
    while count_F >= 3:
        count_F -= 3
        cost += 2 * sku_map['F']
    return cost + count_F * sku_map['F']

