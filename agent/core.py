import os 
from dotenv import load_dotenv
from agent.tools import buscar_web                                                          
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent                                                        
load_dotenv()

agent = create_agent(
    model=ChatOpenAI(model="gpt-4o-mini"),
    tools=[buscar_web],
    system_prompt="Eres un investigador de temas diversos y tu tarea es ayudar a las personas con sus preguntas, cuentas con una tool que te ayuda a buscar en la web, usala cuando no conozcas la respuesta o te pregunten datos especificos, datos despues de tu fecha de entrenamiento o no estés seguro de la respuesta, debes responder en español."
)

query = input("Que quieres buscar hoy?")
result = agent.invoke({"messages": [("user", query)]})
print(result["messages"][-1].content)