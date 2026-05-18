import requests
api_key = "7358d83d766f45ee76ab09028755362c"

# City name
city = "Delhi"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
print(data)
if response.status_code == 200:

    print("City:", data["name"])

    print("Temperature:", data["main"]["temp"], "°C")

    print("Weather:", data["weather"][0]["description"])

else:
    print("Error:", data["message"])