import json
import urllib3


def header():
    return ('{} {} {}\n' + "=" * 45).format('City'.ljust(10),
                                            'Temperature'.ljust(10),
                                            'Sky description'.ljust(20))


def weather_by_city(city_name):
    try:
        http = urllib3.PoolManager()
        r = http.request('GET',
                         'http://api.openweathermap.org/data/2.5/weather',
                         fields={'q': city_name, 'units': 'metric', 'appid': '2bc3e79bb974a007818864813f53fd35'}
                         )
        data = json.loads(r.data.decode('utf-8'))

        return "{} {} {}".format(data['name'].ljust(10),
                                 str(data['main']['temp']).ljust(10),
                                 str(data['weather'][0]['description']).ljust(20))

    except Exception as e:
        print(e)


print(header())

cities = ['Mombasa', 'Nairobi', 'Kisumu', 'Mandera', 'Arusha', 'Dodoma', 'Kigoma']

for city in cities:
    print(weather_by_city(city))
