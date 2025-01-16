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

    number_of_free_Bs = sku_counts['E'] // 2
    sku_counts['B'] -= number_of_free_Bs

    for k, v in sku_counts.items():
        if k == 'A':
            totalCost += (v % 3) * sku_map[k] + (v //3) * 130
        elif k == 'B':
            totalCost += (v % 2) * sku_map[k] + (v // 2) * 45
        else:
            totalCost += v * sku_map[k]
    
    return totalCost

def 

