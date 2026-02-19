def select_mode(mode: str):
    
    #Returns active module name.

    mode = mode.lower()

    if mode == "precropping":
        return "budget + crop suitability"

    if mode == "cropping":
        return "disease + technique support (vision optional)"

    if mode == "postcropping":
        return "yield + selling + policy support"

    return "unknown"
