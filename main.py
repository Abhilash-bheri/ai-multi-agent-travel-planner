import os
import json
from dotenv import load_dotenv
from typing import Annotated,TypedDict,List
import operator
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START,END,StateGraph
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage,BaseMessage
from tools.filigt_tool import search_flights
from tools.tavily_tool import tavily_search
load_dotenv()
from pydantic import BaseModel

class TripInfo(BaseModel):
    departure: str
    arrival: str
    city: str
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=os.getenv("GOOGLE_API_KEY"))

class TravelState(TypedDict):
    messages : Annotated[List[BaseMessage],operator.add]
    user_query:str
    flight_results:str
    hotel_results:str
    itinerary:str
    # llm_calls:int
    result:str
    departure: str
    arrival: str
    city: str

def initial(state:TravelState):
    structured_llm = llm.with_structured_output(TripInfo)

    data = structured_llm.invoke(state["user_query"])

    return {
        "departure": data.departure,
        "arrival": data.arrival,
        "city": data.city,
    }
def flight_agent(state:TravelState):
    """"""
    query=state["user_query"]
    flight_data=search_flights(state["departure"],state["arrival"])
    return {
        "flight_results":flight_data,
        "messages":[
        AIMessage(content=f"flight results fetched")],
        "llm_calls":state.get("llm_calls",0)+1
    }


def hotel_agent(state:TravelState):
    """IT will Call Tavily search and give the best hotels in the city your searching"""
    query = f"Best hotels in {state['city']}"
    hotel_results=tavily_search(query)
    return {
        "hotel_results":hotel_results,
        "messages":[
            AIMessage(content="Hotel Information fetched")
        ],
        "llm_calls":state.get("llm_calls",0)+1
    }


def itinerary(state:TravelState):
    """Generates a travel itinerary."""
    return

def final_agent(state:TravelState):
    """Returns the final travel response."""
    res=f"""from this information make an best plan for user {state["flight_results"] , state["hotel_results"]} and user query {state["user_query"]}"""
    result=llm.invoke(res).content
    return {
    "result": result,
    "departure": state["departure"],
    "arrival": state["arrival"],
    "city": state["city"],
    "flight_results": state["flight_results"],
    "hotel_results": state["hotel_results"],
    }

graph=StateGraph(TravelState)
graph.add_node("flight_agent",flight_agent)
graph.add_node("hotel_agent",hotel_agent)
graph.add_node("itinerary",itinerary)
graph.add_node("final_agent",final_agent)
# graph.add_edge(START,"flight_agent")
# graph.add_edge("flight_agent","hotel_agent")
# graph.add_edge("hotel_agent","final_agent")
# graph.add_edge("final_agent",END)
graph.add_node("initial",initial)
graph.add_edge(START,"initial")
graph.add_edge("initial","flight_agent")
graph.add_edge("initial","hotel_agent")
graph.add_edge("hotel_agent","final_agent")
graph.add_edge("flight_agent","final_agent")
graph.add_edge("final_agent",END)

builder=graph.compile()

# result = builder.invoke({
#     "user_query": "make travel plan form hyderabad to delhi",
#     "messages": [],
#     "flight_results": "",
#     "hotel_results": "",
#     "itinerary": "",
#     "llm_calls": 0,
# })

# print(result["result"])