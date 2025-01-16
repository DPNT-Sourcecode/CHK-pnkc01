

# noinspection PyUnusedLocal
# skus = unicode string

skuMap = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}


def checkout(skus):
    skuCounts = defaultDict(int)
    totalCost = 0
    for c in skus:
        if c not in skuMap:
            return -1
        skuCounts[c] += 1
    
    for c in skus:
        if c in skuMap:
            if c in 
            totalCost += sk