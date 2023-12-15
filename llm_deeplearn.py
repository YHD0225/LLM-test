import os
import openai

openai.api_key = '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'
# client = OpenAI(api_key='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')
# account for deprecation of LLM model
import datetime
# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

print(get_completion("What is 1+1?"))