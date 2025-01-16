from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

skuMap = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}


def checkout(skus):
    skuCounts = defaultdict(int)
    totalCost = 0
    for c in skus:
        if c not in skuMap:
            return -1
        skuCounts[c] += 1
    for k, v in skuCounts.items():
        if k == 'A':
            totalCost += (v % 3) * skuMap[k] + (v //3) * 130
        elif k == 'B':
            totalCost += (v % 2) * skuMap[k] + (v // 2) * 45
        else:
            totalCost += v * skuMap[k]
    
    return totalCost
