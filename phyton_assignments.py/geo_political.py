from enum import Enum


class GeoPoliticalZone:
    NORTH_WEST = ["Kano", "Kaduna", "Katsina", "Kebbi", "Sokoto", "Zamfara"]
    NORTH_EAST = ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"]
    NORTH_CENTRAL = ["Benue", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau", "FCT"]
    SOUTH_WEST = ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"]
    SOUTH_SOUTH = ["Akwa Ibom", "Bayelsa", "Cross River", "Rivers", "Delta", "Edo"]
    SOUTH_EAST = ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"]

    def get_states(zone: str) -> object:
        return getattr(GeoPoliticalZone, zone)

    @staticmethod
    def get_geo_political_zone(state: str):
        for zones in dir(GeoPoliticalZone):
            if not zones.startswith("."):
                state_s = GeoPoliticalZone.get_states(zones)
                if state.lower() in (check.lower() for check in state_s):
                    return zones, state_s
        return None, None


if __name__ == "__main__":
    input_state = input("Enter a state name: ").strip()
    zone, states = GeoPoliticalZone.get_geo_political_zone(input_state)
    if zone:
        print(f"{input_state} belongs to the {zone.lower().replace('_', ' ')} geopolitical zone.")
        print("States in the same zone: " + ", ".join(states))
    else:
        print(f"Could not determine the geopolitical zone for {input_state}.")
