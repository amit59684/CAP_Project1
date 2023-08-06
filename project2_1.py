import requests

def weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    i = requests.get(url)

    if i.status_code == 200:
        data = i.json()
        kelvin = data["main"]["temp"]
        celsius = kelvin - 273.15
        return celsius
if __name__ == "__main__":
    api_key = "ed418c43728bef329f36289091319fc4"
    city = input("Please Enter the city name: ")
    temperature = weather_data(api_key, city)
    temperature=int(temperature)
    if temperature :
        print(f"The temperature in {city} is {temperature}°C.")
    else:
        print("Plese check city name")    
