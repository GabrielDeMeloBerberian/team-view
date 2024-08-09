# This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Author: Gabriel De Melo Berberian

from bs4 import BeautifulSoup


def load_template(template_path):
    with open(template_path, "r", encoding="utf-8") as template_file:
        return template_file.read()


def generate_collapsible_content(data):
    team_template = load_template("resource/template/team_template.html")

    def create_attribute_element(key, value):
        div_content = f"<div class=\"attribute\"><b>{key.capitalize()}:</b>"
        opened_paragraph = False
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for sub_name, sub_info in item.items():
                        if isinstance(sub_info, dict):
                            div_content += generate_team_element(sub_name, sub_info)
                            if opened_paragraph:
                                div_content += '</p>'
                                opened_paragraph = False
                        else:
                            if not opened_paragraph:
                                div_content += '<p>'
                                opened_paragraph = True
                            div_content += f"<span title=\"{sub_info}\" class=\"hoverable\">{sub_name}  &#8505;</span>"
                else:
                    if not opened_paragraph:
                        div_content += '<p>'
                        opened_paragraph = True
                    div_content += f"<span>{item}</span>"
            if opened_paragraph:
                div_content += '</p>'
        elif isinstance(value, dict):
            div_content += generate_team_element(key, value)
        else:
            div_content += f"<p class=\"text\">{value}</p>"

        div_content += "</div>"
        return div_content

    def generate_team_element(name, info, initially_active=False):
        team_element = (team_template
                        .replace("{{ team_name }}", name)
                        .replace("{{ initially_active }}", " initially_active" if initially_active else ''))
        dynamic_content = ""

        for key, value in info.items():
            dynamic_content += create_attribute_element(key, value)

        team_element = team_element.replace("{{ dynamic_content }}", dynamic_content)
        return team_element

    team_elements = [generate_team_element(name, info, initially_active=True) for name, info in data.items()]
    return "\n".join(team_elements)


def to_collapsible_html(data):
    # Load the main HTML template
    with open("resource/template/teams_template.html", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    # Generate the collapsible content
    content = generate_collapsible_content(data)

    # Replace placeholder with the generated content
    html_content = template.replace("{{ content }}", content)

    # Parse the HTML and prettify it
    soup = BeautifulSoup(html_content, "html.parser")
    pretty_html_content = soup.prettify()

    return pretty_html_content
