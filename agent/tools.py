from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv()


# Initialize the Tavily Search tool
tavily_search = TavilySearch(max_results=5, topic="general")

@tool 
def buscar_web(query: str) -> str: 
    """Esta herramienta busca información actual en internet usando Tavily.                                             
    Úsala cuando la pregunta requiera datos recientes, hechos específicos,                           
    o información posterior a tu fecha de corte de entrenamiento o cosas que no sepas responder."""      
    result = tavily_search.invoke({"query": query})
    output = ""
    for dato in result['results']:
        output += f"Título: {dato['title']}\nContenido: {dato['content']}\nURL: {dato['url']}"         
    return output

                                                                                                 
if __name__ == "__main__":                                                                       
      resultado = buscar_web.invoke({"query": "Canada immigration policy 2026"})                 
      print(resultado)       