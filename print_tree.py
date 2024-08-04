# This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Author: Gabriel De Melo Berberian

# Parse JSON to tree format
def to_tree(data, indent="", is_last=True):
    result = []
    if isinstance(data, dict):
        for i, (key, value) in enumerate(data.items()):
            connector = "└── " if is_last and i == len(data) - 1 else "├── "
            result.append(indent + connector + key)
            result.extend(to_tree(value, indent + ("    " if is_last and i == len(data) - 1 else "│   "),
                                  is_last=(i == len(data) - 1)))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                for sub_key, sub_value in item.items():
                    connector = "└── " if is_last and i == len(data) - 1 else "├── "
                    result.append(indent + connector + sub_key)
                    result.extend(to_tree(sub_value, indent + ("    " if is_last and i == len(data) - 1 else "│   "),
                                          is_last=(i == len(data) - 1)))
            else:
                connector = "└── " if is_last and i == len(data) - 1 else "├── "
                result.append(indent + connector + str(item))
    else:
        result.append(indent + "└── " + str(data))
    return result
