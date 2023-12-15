import os
import openai

# openai.api_key = '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'
openai.api_key = 'sk-gLYd9kQMK0EOqmwjRojOT3BlbkFJc3hesLf8mT6AuI0'

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

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""

prompt = f"""Translate the text \
that is delimited by triple backticks
into a style that is {style}.
text: ```{customer_email}```
"""

# print(prompt)
response = get_completion(prompt)
print(response)

prompt = '请介绍一下蔚来汽车公司，具体详细'
response = get_completion(prompt)
print(response)


