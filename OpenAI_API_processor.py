import os
from openai import AzureOpenAI
import pandas as pd

openai.api_key = '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'
# client = AzureOpenAI(
#     api_key="7282c43ed0b549118f59d015ccdc467d",  
#     api_version="2023-10-01-preview",
#     azure_endpoint = "https://openapiazconf.openai.azure.com/"
#     )
deployment_name='azconfmodel'

def load_dataset(file_path):
    return pd.read_excel(file_path)

import openai
import pandas as pd

def chat_with_gpt4(dataset=None):

    while True:
        user_input = input("You: ")

        # Check for termination command
        if user_input.lower() in ["stop", "exit"]:
            print("Chat ended.")
            break

        # Check if the question is in the dataset
        if dataset is not None and user_input in dataset['Question'].values:
            answer = dataset[dataset['Question'] == user_input]['Answer'].iloc[0]
            print("Bot:", answer)
        else:
            # Send the question to GPT-4 and get the response
            try:
                response = .completions.create(model=deployment_name, prompt=user_input, max_tokens=20)
                print(response.choices[0].text)
            except Exception as e:
                print("An error occurred:", e)
                break
