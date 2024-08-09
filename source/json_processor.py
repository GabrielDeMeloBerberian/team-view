# This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Author: Gabriel De Melo Berberian

# Process json in order to remove specified attributes
def process_json(data,
                 remove_mission=True,
                 remove_responsibilities=True,
                 remove_responsible=True,
                 remove_collaborators=True,
                 remove_channels=True):
    if isinstance(data, dict):
        if remove_mission and "mission" in data:
            del data["mission"]
        if remove_responsibilities and "responsibilities" in data:
            del data["responsibilities"]
        if remove_responsible and "responsible" in data:
            del data["responsible"]
        if remove_channels and "channels" in data:
            del data["channels"]
        if remove_collaborators and "collaborators" in data:
            del data["collaborators"]
        for key, value in data.items():
            process_json(
                value,
                remove_mission,
                remove_responsibilities,
                remove_responsible,
                remove_collaborators,
                remove_channels)
    elif isinstance(data, list):
        for item in data:
            process_json(
                item,
                remove_mission,
                remove_responsibilities,
                remove_responsible,
                remove_collaborators,
                remove_channels)
    return data
