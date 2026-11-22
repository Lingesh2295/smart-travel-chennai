def metro_fare(distance_km: float):
    """
    Chennai Metro approximate fare logic
    """
    if distance_km <= 5:
        return 20
    elif distance_km <= 12:
        return 30
    elif distance_km <= 24:
        return 40
    else:
        return 50


def bus_fare():
    """
    MTC bus average fare
    """
    return 25


def auto_fare(distance_km: float):
    """
    Chennai auto fare estimation
    """
    base_fare = 25        # first 1.8 km
    per_km_rate = 15

    if distance_km <= 1.8:
        return base_fare

    extra_distance = distance_km - 1.8
    return int(base_fare + extra_distance * per_km_rate)


def cab_fare(distance_km: float):
    """
    Cab fare estimation (Ola / Uber average)
    """
    base_fare = 50
    per_km_rate = 12

    return int(base_fare + distance_km * per_km_rate)
