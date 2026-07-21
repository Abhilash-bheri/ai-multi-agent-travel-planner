import os
from dotenv import load_dotenv
import requests
load_dotenv()
def search_flights(dep,arr):
    flights=[]
    url = "https://api.aviationstack.com/v1/flights"
    params={
        "access_key":os.getenv("AVIATIONSTACK_API_KEY"),
        "dep_iata":dep,
        "arr_iata":arr,
        "limit":5
    }
    responce=requests.get(url,params=params)
    data=responce.json()
    for flight in data["data"]:
        airline=flight.get("airline").get("name")
        departure=flight.get("departure").get("airport")
        arrival=flight.get("arrival").get("airport")
        status=flight.get("flight_status")
        dep_time=flight.get("departure", {}).get("scheduled")
        flights.append(f"""
                        Airline:{airline},
                        Departure:{departure},
                        Arrival:{arrival},
                        Status:{status},
                        "departure_time":{dep_time},
                       """)
    return "\n\n".join(flights)

search_flights("DEL","BOM")