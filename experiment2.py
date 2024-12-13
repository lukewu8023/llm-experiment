import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

os.environ['OPENAI_API_BASE'] = 'https://api.ohmygpt.com/v1/'
os.environ['OPENAI_API_KEY'] = ''

model = 'gpt-4o-mini'

chat = ChatOpenAI(model=model, temperature=0.1, verbose=True)    

request = "Who are you?"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
output_parser = StrOutputParser()
chain = prompt | chat | output_parser
response = chain.invoke(
    {
        "messages": [
            HumanMessage(content=request),
        ],
    }
)

print(response)