K_FACTOR = 20


def calculate_rating_change(result):
    if result == "win":
        return 20

    if result == "draw":
        return 5

    return -10
