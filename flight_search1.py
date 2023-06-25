import requests
from flight_data1 import FlightData
from details import api_key_tequila
api_key = api_key_tequila
tequila_endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:
    def get_destination_code(self,city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey": api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url = location_endpoint,headers = headers, params = query)
        results = response.json()['locations']
        code = results[0]['code']
        # print(code)
        return code
    # This class is responsible for talking to the Flight Search API.

    def check_flights(self,og_city_code,destination_city_code, from_time, to_time):
        headers = {'apikey': api_key}
        query = {
            'fly_from': og_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 14,
            "flight_type": 'round',
            'one_for_city': 1,
            'max-stopovers': 0,
            'curr': 'INR'
        }
        response = requests.get(url = f"{tequila_endpoint}/v2/search", headers= headers,params  =query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {destination_city_code}.')
            return None

        flight_data = FlightData( price = data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city} : {flight_data.price} rupees")
        return flight_data
