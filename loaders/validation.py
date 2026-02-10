def validate_district(district_name, dataset):
    """
    Checks if district exists in given dataset list.
    """

    for entry in dataset:
        if entry["district"].lower() == district_name.lower():
            return True

    return False
