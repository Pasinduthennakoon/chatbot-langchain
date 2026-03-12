from fastapi import FastAPI
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel
from chain import chain, history 

app = FastAPI()

class Question(BaseModel):
    question: str
    
@app.post('/ask')
async def ask(question: Question):
    response = chain.invoke({'history': history, 'question': [HumanMessage(content=question.question)]})
    history.extend([HumanMessage(content=question.question), AIMessage(content=response)])
    return {'response': response}
