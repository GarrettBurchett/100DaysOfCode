#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import date, timedelta
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(dotenv_path=Path("./Day39-40/.env"))
ORIGIN_CITY_IATA = "YOUR STARTING CITY HERE"
tomorrow = date.today() + timedelta(days=1)
from_date = tomorrow.strftime('%d/%m/%Y')
to_date = (tomorrow + timedelta(days=180)).strftime('%d/%m/%Y')

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_rows()

if sheet_data[0]['iataCode'] == '':
    
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_row()

NoneType = type(None)
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=from_date,
        to_time=to_date
    )

    if not isinstance(flight, NoneType):
        if flight.price < destination['lowestPrice']:
            users = data_manager.get_emails()
            emails = [row['email'] for row in users]

            message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"

            notification_manager.send_emails(message, emails)