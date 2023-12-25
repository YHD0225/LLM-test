import os
import openai

# openai.api_key = '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'
openai.api_key = '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'
openai_api_key = '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'
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

def get_completion(system_prompt,prompt, model=llm_model):
    messages = [
        {"role":"system","content":system_prompt},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
system_prompt = """You are a large language model. Now you act as a mature driving assistant, who can give accurate and correct advice for human driver in complex urban driving scenarios.You will be given a detailed description of the driving scenario of current frame along with your history of previous decisions. You will also be given the available actions you are allowed to take.

All of these elements are delimited by ####.
Your response should use the following format:
<reasoning>
<reasoning>
<repeat until you have a decision>
Response to user:#### <only output one `Action_id` as a int number of you decision, without any action name or explanation. The output decision must be unique and not ambiguous, for example if youdecide to decelearate, then output `4`>

Make sure to include #### to separate every step."""

user_prompt = """Here is the current scenario:

#### Driving scenario description: 
You are driving on a road with 2 lanes, and you are currently
driving in the leftmost lane. Your current position is `(0.00,
0.00)`, speed is 14.12 $m/s$, acceleration is -0.5 $m/s^2$, and
lane position is 0.00 $m$. There are other vehicles driving around 
you, and below is their basic information:
- Vehicle `a` is driving on the lane to your right and is ahead
of you. The position of it is `(54.91, -3.77)`, speed is 9.08
$m/s$, acceleration is -0.02 $m/s^2$, and lane position is -3.3
$m$.
- Vehicle `b` is driving on the lane to your right and is behind
of you. The position of it is `(-13.53,-3.14)`, speed is 10.25
$m/s$, acceleration is 0.32 $m/s^2$, and lane position is -3.3
$m$.

#### Driving Intensions: 
Your driving intension is to drive safely and avoid collisions and fast.

#### Available actions: 
IDLE - remain in the current lane with current speed Action_id: 1
Turn-right - change lane to the right of current lane Action_id: 2

You can stop reasoning once you have a valid action to take."""

print(get_completion(system_prompt,user_prompt))

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

# prompt = '请介绍一下蔚来汽车公司，具体详细'
# response = get_completion(prompt)
# print(response)

from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0.0, model=llm_model)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(template_string)

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

customer_response = chat(customer_messages)

print(customer_response.content)











