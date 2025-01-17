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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

multi_buy_deals = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 120)],
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

group_discounts = [(['S', 'T', 'X', 'Y', 'Z'], 3, 45)]

def checkout(skus):
    sku_counts = defaultdict(int)
    totalCost = 0
    for c in skus:
        if c not in sku_map:
            return -1
        sku_counts[c] += 1

    for sku, deal in buy_get_free_deals.items():
        if sku in sku_counts:
            use_buy_get_free_deal(sku_counts, sku, deal)

    for sku, deals in multi_buy_deals.items():
        if sku in sku_counts:
            totalCost += calculate_multibuy_cost(sku_counts[sku], sku, deals)
            sku_counts[sku] = 0

    totalCost += use_group_discount(sku_counts, group_discounts)

    for k, v in sku_counts.items():
            totalCost += v * sku_map[k]

    return totalCost

def calculate_multibuy_cost(count, sku, deals):
    cost = 0
    for qty, price in sorted(deals, reverse=True):
        while count >= qty:
            cost += price
            count -= qty
    cost += count * sku_map[sku]
    return cost

def use_buy_get_free_deal(sku_counts, sku, buy_get_free_deal):
    other_sku, buy, free = buy_get_free_deal
    count = sku_counts[sku]
    free_count = 0

    if other_sku == sku:
        a = sku_counts[sku] // (buy + free)
        free_count = a * free
        sku_counts[sku] -= free_count
    elif other_sku in sku_counts:
        free_count = (sku_counts[other_sku] // buy) * free
    sku_counts[sku] = max(0, count - free_count)

def use_group_discount(sku_counts, group_discounts):
    cost = 0

    for group, qty, price in group_discounts:
        group_items = [(itm, sku_map[itm], sku_counts[itm]) for itm in group if sku_counts[itm] > 0]
        group_items.sort(key=lambda x: x[1], reverse=True)

        total = sum(item[2] for item in group_items)

        count_discounts = total // qty
        
        cost += count_discounts*price

        handle_count = count_discounts * qty
        for i, (item, _, cnt) in enumerate(group_items):
            if handle_count <= 0:
                break
            consumed = min(cnt, handle_count)
            sku_counts[item] -= consumed
            handle_count -= consumed
    return cost



