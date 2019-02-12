# Python program to find current
# weather details of any city
# using openweathermap api

import requests, json

def lambda_handler(event, context):
    # city_name = event['Details']['Parameters']['City']
    city_name = "Boston"
    result = get_weather(city_name)
    return {
        'weather': result
    }

def get_weather(city_name):
    # api_key = "160b9ec57af67eb385e26055c85dbff0"
    api_key = "886705b4c1182eb1c69f28eb8c520e20"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    result = response.json()

    # print result

    if result["cod"] == 200:
        main_res = result["main"]
        current_temperature = main_res["temp"] # in kelvin unit
        current_pressure = main_res["pressure"] # in hPa unit
        current_humidiy = main_res["humidity"] # in percentage
        weather_description = result["weather"][0]["description"] # "snow", "clear sky", etc

        return weather_description

        print "The weather in " + city_name + " is: "
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
                         str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description))
    else:
        return None

        print(" City Not Found ")

if __name__ == "__main__":
    print lambda_handler(None, None)
