from datetime import datetime, timedelta
from flight_search1 import FlightSearch
from data_manager1 import DataManager
from notification_manager1 import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DEL"

if sheet_data[0]['iataCode']=="":
    from flight_search1 import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days = 1)
six_months_from_today = datetime.now() + timedelta(days = 180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time = tomorrow,
        to_time = six_months_from_today
    )
    if flight.price< destination['lowestPrice']:
        notification_manager.send_sms(
        message=f"Low price alert! Only {flight.price} rupees to fly from {flight.departure_city}-{flight.departure_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    )
