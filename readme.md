# Team View

## Summary

- [Description](#description)
- [Required Tools](#required-tools)
- [Local Setup and Execution](#local-setup-and-execution)
    - [Arguments](#arguments)
    - [Example](#example)
- [License](#license)
- [Author](#author)

## Description

The **Team View** is a tool designed to allow you to view your organization's teams in a hierarchical intuitive way and
filter the right information.

## Required Tools

To run this project, you will need the following tools:

- [Python 3.x](https://www.python.org/downloads/)

## Local Setup and Execution

Follow the steps below to set up the local development environment:

1. Clone the repository:
    ```sh
    git clone https://github.com/GabrielDeMeloBerberian/team-view.git
    cd team-view
    ```

2. Run the project using the command below followed by the necessary arguments:
    ```sh
    python main.py [ARGUMENTS]
    ```

### Arguments

| Argument                 | Description                        | Type      | Required | Example                       |
|--------------------------|------------------------------------|-----------|----------|-------------------------------|
| `-i, --input`            | Path to the input JSON file        | `str`     | Yes      | `--input data/input.json`     |
| `-o, --output`           | Path to the output file            | `str`     | Yes      | `--output results/output.txt` |
| `-m, --mission`          | Keep `mission` attributes          | `boolean` | Yes      | `--mission`                   |
| `-r, --responsibilities` | Keep `responsibilities` attributes | `boolean` | No       | `--responsibilities`          |
| `-R, --responsible`      | Keep `responsible` attributes      | `boolean` | No       | `--responsible`               |
| `-C, --collaborators`    | Keep `collaborators` attributes    | `boolean` | No       | `--collaborators`             |
| `-c, --channels`         | Keep `channels` attributes         | `boolean` | No       | `--channels`                  |

### Example

```sh
python main.py --input input.json --output output.txt -m -r -R -C -c
```

#### Example Input

Contents of `input.json`:

```json
{
  "project": {
    "name": "Team View",
    "mission": "Organize team views",
    "responsibilities": [
      "Planning",
      "Execution"
    ],
    "responsible": "Gabriel Berberian",
    "collaborators": [
      "Gabriel Berberian",
      "Kate Brown"
    ],
    "channels": [
      "Email: contact@teamview.com",
      "Slack: #team_view"
    ],
    "divisions": [
      {
        "name": "Innovation Team",
        "mission": "Plan new features",
        "responsible": "Jade Green",
        "responsibilities": [
          "Business Requirements Documents (BRD)"
        ],
        "collaborators": [
          "Jade Green",
          "Layla Wood"
        ],
        "channels": [
          "Email: innvovation@teamview.com",
          "Slack: #innovation"
        ]
      },
      {
        "name": "Engineering Team",
        "mission": "Implement features and improvements",
        "responsibilities": [
          "Team View software",
          "Technical Specification Document (TSD)"
        ],
        "responsible": "Quica Black",
        "collaborators": [
          "Quica Black",
          "Luna Yang"
        ],
        "channels": [
          "Email: engineering@teamview.com",
          "Slack: #engineering"
        ]
      }
    ]
  }
}
```

#### Example Output

Contents of `output.txt`:

```
└── Team View
    ├── mission
    │   └── Organize team views
    ├── responsibilities
    │   ├── Planning
    │   ├── Execution
    ├── responsible
    │   └── Gabriel Berberian
    ├── collaborators
    │   ├── Gabriel Berberian
    │   ├── Kate Brown
    ├── channels
    │   ├── Email: contact@teamview.com
    │   ├── Slack: #team_view
    └── divisions
        ├── Innovation Team
        │   ├── mission
        │   │   └── Plan new features
        │   ├── responsible
        │   │   └── Jade Green
        │   ├── responsibilities
        │   │   ├── Business Requirements Documents (BRD)
        │   ├── collaborators
        │   │   ├── Jade Green
        │   │   ├── Layla Wood
        │   ├── channels
        │   │   ├── Email: innvovation@teamview.com
        │   │   └── Slack: #innovation
        └── Engineering Team
            ├── mission
            │   └── Implement features and improvements
            ├── responsibilities
            │   ├── Team View software
            │   ├── Technical Specification Document (TSD)
            ├── responsible
            │   └── Quica Black
            ├── collaborators
            │   ├── Quica Black
            │   ├── Luna Yang
            └── channels
                ├── Email: engineering@teamview.com
                └── Slack: #engineering
```

## License

This work is licensed under
the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Author

[Gabriel De Melo Berberian](https://github.com/GabrielDeMeloBerberian)