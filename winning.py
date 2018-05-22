def winning_type(numbersList):
    """determine the winning type for a list of integers"""
    if numbersList == []:
        return "No items"

    items = []
    counter = 0
    for item in numbersList:
        if item not in items:
            items.append(item)
        else:
            counter += 1

    if counter == 1:
        return "small win"
    elif counter == 2:
        return "big win"
    else:
        return "no win"