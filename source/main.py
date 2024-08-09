# This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Author: Gabriel De Melo Berberian

import json
import argparse
from json_processor import process_json
from tree_generator import to_tree
from collapsible_html_generator import to_collapsible_html


def main(
        input_path,
        output_path,
        tree_format,
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

    if tree_format:
        result = "\n".join(to_tree(data))
    else:
        if not output_path.endswith('.html'):
            output_path += '.html'
        result = to_collapsible_html(data)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON and print it in tree or collapsible format.")
    parser.add_argument("-i", "--input", required=True, help="Input JSON file path.")
    parser.add_argument("-o", "--output", required=True, help="Output file path.")
    parser.add_argument("-t", "--tree", action="store_true",
                        help="Output in tree format if the argument is informed. Otherwise, the output is default to HTML format with collapsible elements.")
    parser.add_argument("-m", "--mission", action="store_true", help="Keep 'mission' attributes.")
    parser.add_argument("-r", "--responsibilities", action="store_true", help="Keep 'responsibilities' attributes.")
    parser.add_argument("-R", "--responsible", action="store_true", help="Keep 'responsible' attributes.")
    parser.add_argument("-C", "--collaborators", action="store_true", help="Keep 'collaborators' attributes.")
    parser.add_argument("-c", "--channels", action="store_true", help="Keep 'channels' attributes.")
    args = parser.parse_args()

    main(
        args.input,
        args.output,
        args.tree,
        args.mission,
        args.responsibilities,
        args.responsible,
        args.collaborators,
        args.channels)
