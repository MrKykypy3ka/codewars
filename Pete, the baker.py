def cakes(recipe, available):
    count = 0
    while True:
        for key in recipe:
            if key not in available:
                return count
            if available[key] < recipe[key]:
                return count
            else:
                available[key] -= recipe[key]
        count += 1