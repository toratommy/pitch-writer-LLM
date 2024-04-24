import os
import openai
from langchain.llms import OpenAI as LLMOpenAI  # Using an alias to avoid confusion with openai import
from langchain.prompts import PromptTemplate

openai.api_key = 'your-openai-api-key'

def read_files(directory):
    file_contents = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                file_contents.append(file.read())
    return file_contents

def generate_pitch(base_texts, new_project_description):
    # Initialize the OpenAI client from LangChain
    llm_openai = LLMOpenAI(api_key=openai.api_key)

    # Prepare the context from previous texts
    context = " ".join(base_texts)

    # Create a prompt template with dynamic input
    prompt_template = PromptTemplate(
        template_string="Given the following project details: {}\nGenerate a detailed pitch based on the historical context provided.",
        llim=llm_openai
    )

    # Generate the pitch using the prompt template
    new_pitch = prompt_template.generate([new_project_description], context=context)
    return new_pitch

def main():
    directory_of_past_pitches = 'path/to/your/past/pitches'
    description_of_new_project = 'path/to/new/project/description.txt'

    # Read past pitches and project descriptions
    past_pitches = read_files(directory_of_past_pitches)
    with open(description_of_new_project, 'r') as file:
        new_project_description = file.read()

    # Generate the new pitch
    new_pitch = generate_pitch(past_pitches, new_project_description)
    print("Generated Pitch:")
    print(new_pitch)

if __name__ == "__main__":
    main()
