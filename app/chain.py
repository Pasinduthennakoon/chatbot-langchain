from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import  SystemMessage
from langchain_core.output_parsers import StrOutputParser
from config import GOOGLE_API_KEY
import os

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    temperature = 0
)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='You are an intelligent chatbot.Answer the following question.'),
        MessagesPlaceholder(variable_name='history'),
        MessagesPlaceholder(variable_name='question')
    ]
)

history = []

parser = StrOutputParser()

chain = prompt | llm | parser