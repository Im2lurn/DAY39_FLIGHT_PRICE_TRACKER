import requests
from details import headers
url = "https://api.sheety.co/2ced0d42e333907d25c9d9590e078d71/ishita'sCopyOfFlightDeals/prices"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url = f"{url}/{city['id']}",headers=headers, json = new_data)
            print(response.text)


    def get_destination_data(self):
        response = requests.get(url, headers=headers)
        sheet_data = response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data

