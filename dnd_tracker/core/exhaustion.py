#Logic/rules for exhaustion tracking

def food_needed(miles:float, rate_per_mile:float) -> float:
    """
    Calculate the amount of food needed based on miles traveled and rate per mile.

    :param miles: The number of miles traveled.
    :param rate_per_mile: The amount of food consumed per mile.
    :return: The total amount of food needed.
    """
    return miles * rate_per_mile
