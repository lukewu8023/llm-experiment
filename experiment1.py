import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

os.environ['OPENAI_API_BASE'] = 'https://api.ohmygpt.com/v1/'
os.environ['OPENAI_API_KEY'] = ''

model = 'gpt-4o-mini'

chat = ChatOpenAI(model=model, temperature=0.1, verbose=True)    

request = "Who are you?"

messages = [
    HumanMessage(request),
]

response = chat.invoke(messages)

print(response)