# Team View

## Summary

- [Description](#description)
- [Required Tools](#required-tools)
- [Local Setup and Execution](#local-setup-and-execution)
    - [Arguments](#arguments)
    - [Examples](#examples)
      - [Input](#input)
      - [Output](#output)
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

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the project using the command below followed by the necessary arguments:
    ```sh
    python source/main.py [ARGUMENTS]
    ```

### Arguments

| Argument                 | Description                                                                                           | Type      | Required | Example                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------|-----------|----------|-----------------------------------------|
| `-i, --input`            | Path to the input JSON file.                                                                          | `str`     | Yes      | `--input resource/input/sample.json`    |
| `-o, --output`           | Path to the output file.                                                                              | `str`     | Yes      | `--output resource/input/sample_output` |
| `-t, --tree`             | Set tree format for output. If not present, output format is set to html (with collapsible elements). | `boolean` | No       | `--tree`                                |
| `-m, --mission`          | Keep `mission` attributes.                                                                            | `boolean` | No       | `--mission`                             |
| `-r, --responsibilities` | Keep `responsibilities` attributes.                                                                   | `boolean` | No       | `--responsibilities`                    |
| `-R, --responsible`      | Keep `responsible` attributes.                                                                        | `boolean` | No       | `--responsible`                         |
| `-C, --collaborators`    | Keep `collaborators` attributes.                                                                      | `boolean` | No       | `--collaborators`                       |
| `-c, --channels`         | Keep `channels` attributes.                                                                           | `boolean` | No       | `--channels`                            |

### Examples

#### Input

Content of `resource/input/sample.json`:

```json
{
  "Team View": {
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
      {
        "Slack: #teamview": "Channel to talk about Team View"
      }
    ],
    "divisions": [
      {
        "Innovation Team": {
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
            {
              "Slack: #innovation": "Channel to talk about innovation"
            }
          ]
        }
      },
      {
        "Engineering Team": {
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
            {
              "Slack: #engineering": "Channel to talk about engineering"
            }
          ]
        }
      }
    ]
  }
}
```

#### Output

With `--tree` argument:

```sh
python source/main.py --input resource/input/sample.json --output resource/input/sample_output.txt -t -m -r -R -C -c
```

Content of `resource/input/sample_output.txt`:

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
    │   ├── Slack: #teamview
    │   │   └── Channel to talk about Team View
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
        │   │       └── Channel to talk about innovation
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
                    └── Channel to talk about engineering
```

Without `--tree` argument:

```sh
python source/main.py --input resource/input/sample.json --output resource/input/sample_output -m -r -R -C -c
```

Content of `resource/input/sample_output.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <title>
        Team Collapsible View
    </title>
    <style>
        body {
               font: 15px Arial
             }
     
             .team {
               border: 1px solid #777;
               border-radius: 18px;
               display: flex;
               flex-direction: column;
               min-width: 100%;
               box-sizing: border-box;
             }
     
             .collapsible {
               background-color: #777;
               color: white;
               cursor: pointer;
               padding: 18px;
               width: 100%;
               border: none;
               text-align: left;
               outline: none;
               font-size: 15px;
               border-radius: 18px;
             }
     
             .collapsible:hover {
               background-color: #555;
             }
     
             .active {
               background-color: #555;
               border-radius: 18px 18px 0 0;
             }
     
             .collapsible:after {
               content: '\002B';
               color: white;
               font-weight: bold;
               float: right;
               margin-left: 5px;
             }
     
             .active:after {
               content: "\2212";
             }
     
             .content {
               padding: 0 18px;
               max-height: 0;
               overflow: hidden;
               transition: max-height 0.2s ease-out;
               background-color: #f1f1f1;
               border-radius: 0 0 18px 18px;
             }
     
             .attribute > * {
               display: flex;
               flex-wrap: wrap;
               margin-block-start: 1em;
               margin-block-end: 1em;
               margin-inline-start: 0px;
               margin-inline-end: 0px;
               unicode-bidi: isolate;
             }
     
             span {
               display: inline-block;
               background-color: lightgray;
               border: solid gray 1px;
               margin: 0 1em 1em 0;
               padding: 3px;
               border-radius: 3px;
               white-space: nowrap;
               line-height: normal;
               vertical-align: baseline;
             }
     
             .hoverable:hover {
               background-color: gray;
               color: white;
             }
     
             .text {
                 margin-bottom: 2em;
             }
    </style>
</head>
<body>
<div class="team">
    <button class="collapsible initially_active">
        Team View
    </button>
    <div class="content">
        <div class="attribute">
            <b>
                Mission:
            </b>
            <p class="text">
                Organize team views
            </p>
        </div>
        <div class="attribute">
            <b>
                Responsibilities:
            </b>
            <p>
      <span>
       Planning
      </span>
                <span>
       Execution
      </span>
            </p>
        </div>
        <div class="attribute">
            <b>
                Responsible:
            </b>
            <p class="text">
                Gabriel Berberian
            </p>
        </div>
        <div class="attribute">
            <b>
                Collaborators:
            </b>
            <p>
      <span>
       Gabriel Berberian
      </span>
                <span>
       Kate Brown
      </span>
            </p>
        </div>
        <div class="attribute">
            <b>
                Channels:
            </b>
            <p>
      <span>
       Email: contact@teamview.com
      </span>
                <span class="hoverable" title="Channel to talk about Team View">
       Slack: #teamview  ℹ
      </span>
            </p>
        </div>
        <div class="attribute">
            <b>
                Divisions:
            </b>
            <div class="team">
                <button class="collapsible">
                    Innovation Team
                </button>
                <div class="content">
                    <div class="attribute">
                        <b>
                            Mission:
                        </b>
                        <p class="text">
                            Plan new features
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Responsible:
                        </b>
                        <p class="text">
                            Jade Green
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Responsibilities:
                        </b>
                        <p>
         <span>
          Business Requirements Documents (BRD)
         </span>
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Collaborators:
                        </b>
                        <p>
         <span>
          Jade Green
         </span>
                            <span>
          Layla Wood
         </span>
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Channels:
                        </b>
                        <p>
         <span>
          Email: innvovation@teamview.com
         </span>
                            <span class="hoverable" title="Channel to talk about innovation">
          Slack: #innovation  ℹ
         </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="team">
                <button class="collapsible">
                    Engineering Team
                </button>
                <div class="content">
                    <div class="attribute">
                        <b>
                            Mission:
                        </b>
                        <p class="text">
                            Implement features and improvements
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Responsibilities:
                        </b>
                        <p>
         <span>
          Team View software
         </span>
                            <span>
          Technical Specification Document (TSD)
         </span>
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Responsible:
                        </b>
                        <p class="text">
                            Quica Black
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Collaborators:
                        </b>
                        <p>
         <span>
          Quica Black
         </span>
                            <span>
          Luna Yang
         </span>
                        </p>
                    </div>
                    <div class="attribute">
                        <b>
                            Channels:
                        </b>
                        <p>
         <span>
          Email: engineering@teamview.com
         </span>
                            <span class="hoverable" title="Channel to talk about engineering">
          Slack: #engineering  ℹ
         </span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
    function adjustParentHeight(element, heightChange) {
       var parent = element.parentElement.closest('.content');
       if (parent) {
           parent.style.maxHeight = (parent.scrollHeight + heightChange) + "px";
           adjustParentHeight(parent, heightChange);
       }
     }
 
     function toggleCollapsible(element) {
         element.classList.toggle("active");
         var content = element.nextElementSibling;
         if (content.style.maxHeight) {
             content.style.maxHeight = null;
             adjustParentHeight(content, -content.scrollHeight);
         } else {
             content.style.maxHeight = content.scrollHeight + "px";
             adjustParentHeight(content, content.scrollHeight);
         }
 
         setTimeout(function() {
             element.scrollIntoView({ behavior: "smooth", block: "start" });
         }, 200);
         element.scrollIntoView({ behavior: "smooth", block: "start" });
     }
 
     var collapsibleElements = document.getElementsByClassName("collapsible");
     for (var element of collapsibleElements) {
         element.addEventListener("click", function() {
             toggleCollapsible(this);
         });
     }
 
     window.addEventListener('load', function() {
         var initiallyActiveElements = document.getElementsByClassName("initially_active");
         for (var element of initiallyActiveElements) {
             toggleCollapsible(element);
         }
     });
</script>
</body>
</html>
```

## License

This work is licensed under
the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Author

[Gabriel De Melo Berberian](https://github.com/GabrielDeMeloBerberian)