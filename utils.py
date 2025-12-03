def auto_generate_items(constructs, n_items):
    items = []
    for const in constructs:
        for i in range(1, n_items + 1):
            items.append(f"{const}: {const[:2].upper()}{i}")
    return items
