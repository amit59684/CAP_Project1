import requests

def weather_data(api_key, city):
    get_url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

    if get_url.status_code == 200:
        data = get_url.json()
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
        print("Please check city name you have entered")    
