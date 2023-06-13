!pip install python-weather
import python_weather
import asyncio
import csv

async def get_weather_forecast(location):
    # Declare the client with the default unit set to metric system
    async with python_weather.Client() as client:
        # Fetch the weather forecast for the given location
        weather = await client.find(location)

        # Prepare the forecast data
        forecast_data = []
        for forecast in weather.forecasts:
            forecast_data.append({
                'Date': forecast.date.strftime('%Y-%m-%d'),
                'Temperature': forecast.temperature,
                'Weather Condition': forecast.sky_text
            })

        return forecast_data

def save_forecast_data(data):
    # Save the forecast data in a CSV file
    with open('weather_forecast.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

async def main():
    # Ask the user for the location
    location = input('Enter a location: ')

    try:
        # Get the weather forecast for the next 7 days
        forecast = await get_weather_forecast(location)

        # Print the forecasted temperature and weather conditions for each day
        for day in forecast:
            print(f"Date: {day['Date']}, Temperature: {day['Temperature']}°C, Weather Condition: {day['Weather Condition']}")

        # Save the forecast data in a file
        save_forecast_data(forecast)

    except python_weather.exceptions.BadResponseError:
        print('Error: Failed to retrieve weather data.')
    except Exception as e:
        print(f'Error: {str(e)}')

 async.run(main())
