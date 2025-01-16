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

multi_buy_deals = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 150)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(3, 130), (2, 90)]
}

buy_get_free_deals = {
    'B': ('E', 2, 1),
    'F': ('F', 2, 1),
    'M': ('N', 3, 1),
    'Q': ('R', 3, 1),
    'U': ('U', 3, 1),
}

def checkout(skus):
    sku_counts = defaultdict(int)
    totalCost = 0
    for c in skus:
        if c not in sku_map:
            return -1
        sku_counts[c] += 1

    if 'A' in sku_counts:
        totalCost += calc(sku_counts['A'], 'A', [(5, 200), (3, 130)])
        del sku_counts['A']
    if 'B' in sku_counts:
        totalCost += calculate_B_cost(sku_counts['B'], sku_counts['E'])
        del sku_counts['B']
    if 'F' in sku_counts:
        totalCost += calculate_F_cost(sku_counts['F'])
        del sku_counts['F']


    for sku, count in sku_counts.items():
        if sku in multi_buy_deals:
            totalCost += calculate_multibuy_cost(count, sku, multi_buy_deals[sku])
        if sku in buy_get_free_deals:
            totalCost += calculate_buy_get_free_cost(count, sku, buy_get_free_deals[sku])
            



    for k, v in sku_counts.items():
            totalCost += v * sku_map[k]
    return totalCost

def calculate_multibuy_cost(count, sku, deals):
    cost = 0
    for qty, price in deals:
        while count >= qty:
            cost += price
            count -= qty
    cost += count * sku_map[sku]
    return cost

def calculate_buy_get_free_cost(count, sku, buy_get_free_deal):
    other_sku, buy, free = buy_get_free_deal
    number_to_pay_for = count - other_item_sku // buy
    return (number_to_pay_for % 2) * 30 + (number_to_pay_for // 2) * 45

def calculate_F_cost(count_F):
    cost = 0
    while count_F >= 3:
        count_F -= 3
        cost += 2 * sku_map['F']
    return cost + count_F * sku_map['F']
