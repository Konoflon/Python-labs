import requests

WEATHER_CODES = {
    0: "Ясно", 1: "Преимущественно ясно", 2: "Переменная облачность", 3: "Пасмурно",
    45: "Туман", 51: "Морось", 61: "Дождь", 71: "Снег", 95: "Гроза"
}

def weather_generator(city="Сургут", days=5, lat=61.25, lon=73.40):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto&forecast_days={days}"
    response = requests.get(url)
    data = response.json()
    for i in range(len(data["daily"]["time"])):
        code = data["daily"]["weathercode"][i]
        yield {
            "date": data["daily"]["time"][i],
            "temp_max": data["daily"]["temperature_2m_max"][i],
            "temp_min": data["daily"]["temperature_2m_min"][i],
            "description": WEATHER_CODES.get(code, f"Код {code}"),
            "city": city
        }

def run(city="Сургут", days=5):
    print(f"Lab6: Погода в городе {city} на {days} дней:")
    for day in weather_generator(city, days):
        print(f"{day['date']}: {day['temp_min']}..{day['temp_max']}°C, {day['description']}")