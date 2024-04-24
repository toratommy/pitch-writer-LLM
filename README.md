# Automated Pitch Generation for Consulting Projects

## Introduction
This project provides a Python script designed to automate the creation of pitches for consultancy services. By leveraging the OpenAI API through LangChain, the script utilizes previous project pitches and details about new projects to generate tailored proposals. This automation aims to streamline the process of writing new project pitches, making it efficient and context-aware.

## Requirements
- Python 3.8 or newer
- `openai` Python library
- `langchain` Python library

## Setup
### Installation
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

2. Install Dependencies:
Ensure that Python and pip are installed on your system. Then run:
```bash
pip install -r requirements.txt
```
This command will install the openai and langchain libraries required for the project.

## Configuration
Set your OpenAI API key in your environment to keep it secure:

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

Alternatively, you can directly insert your API key in the script, but be cautious about exposing your key in shared or public environments.

## Usage
To use this script, you must provide:

A directory containing text files of past pitches (`past_pitches_directory`).
A text file containing the description of the new project (`new_project_description.txt`).

### Running the Script
Execute the main script from the command line:

```bash
python generate_pitch.py
```
The script reads the existing pitch documents and the new project description, then generates a pitch tailored to the new project based on historical data.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit pull requests with any enhancements. Make sure to follow the existing coding style and add comments to your code where necessary.

## License
This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Notes
This script assumes the presence of text files in the specified directories. Ensure the paths are correctly set.
The handling of API keys and sensitive information should be done securely, especially in collaborative or public settings.