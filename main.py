# This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Author: Gabriel De Melo Berberian

import json
import argparse
from print_tree import to_tree
from json_processor import process_json


def main(
        input_path,
        output_path,
        keep_mission,
        keep_responsibilities,
        keep_responsible,
        keep_collaborators,
        keep_channels):
    with open(input_path, "r", encoding='utf-8') as infile:
        data = json.load(infile)

    # Process JSON to remove specified attributes
    data = process_json(data,
                        not keep_mission,
                        not keep_responsibilities,
                        not keep_responsible,
                        not keep_collaborators,
                        not keep_channels)

    # Parse JSON to tree format
    result = to_tree(data)

    with open(output_path, "w", encoding='utf-8') as outfile:
        for line in result:
            outfile.write(line + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON and print it in tree format")
    parser.add_argument("-i", "--input", required=True, help="Input JSON file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-m", "--mission", action="store_true", help="Keep 'mission' attributes")
    parser.add_argument("-r", "--responsibilities", action="store_true", help="Keep 'responsibilities' attributes")
    parser.add_argument("-R", "--responsible", action="store_true", help="Keep 'responsible' attributes")
    parser.add_argument("-C", "--collaborators", action="store_true", help="Keep 'collaborators' attributes")
    parser.add_argument("-c", "--channels", action="store_true", help="Keep 'channels' attributes")
    args = parser.parse_args()

    main(
        args.input,
        args.output,
        args.mission,
        args.responsibilities,
        args.responsible,
        args.collaborators,
        args.channels)
