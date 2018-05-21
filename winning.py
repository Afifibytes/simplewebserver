def winning_type(numbersList):
    """determine the winning type for a list of integers"""
    items = []
    counter = 0
    for item in numbersList:
        if item not in items:
            items.append(item)
            counter += 1

    if counter == 1:
        return "big win"
    elif counter == 2:
        return "small win"
    elif counter == 3:
        return "no win"
