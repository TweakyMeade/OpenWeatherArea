import dotenv, paho.mqtt.client as mqtt, os,json, requests 


def portAndKeys():
    global mqttHost
    global mqttPort
    global mqttTopic
    global OWMKey

    dotenv.load_dotenv()

    mqttHost = os.environ.get("Host")
    mqttPort = int(os.environ.get("Port"))
    OWMKey = os.environ.get("OWMkey")
    mqttTopic = 'area'

def weatherRequest(key,location):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?appid={key}&id={location}").json()

def mqttPusher(userHost, userPort, topic,payload):
    client=mqtt.Client()
    client.connect(host=userHost, port=userPort)
    client.publish(topic,payload)

def stringJSONValue(txt):
    return f'\"{txt}\"'

def weatherPayload(weather):
    datetimeR = weather['dt']
    tempR = round(weather['main']['temp']-273.15,2)
    humidR=weather['main']['humidity']
    pressureR= weather['main']['pressure']
    windSpeedR=weather['wind']['speed']
    windDirR=weather['wind']['deg']
    skyR= stringJSONValue(weather['weather'][0]['main'])
    skydescR = stringJSONValue(weather['weather'][0]['description'])
    skyIDR = weather['weather'][0]['id']
    feelsLike = round(weather['main']['feels_like']-273.15,2)
    cityR = stringJSONValue(weather["name"])
    return '{'+f"\"Dateime\":{datetimeR},\"Temperature\":{tempR},\"Humidity\":{humidR},\"WindSpeed\":{windSpeedR},\"WindDirection\":{windDirR},\"Sky\":{skyR},\"Sky Detailed\":{skydescR}, \"Pressure\":{pressureR},\"Tempature feels like\":{feelsLike},\"Location\":{cityR}"+'}'
   
def locationArray():
    with open("location.csv") as loc:
       lArray = []
       for id in loc.read().split(','):
            lArray.append(int(id))
    return lArray


locationID = locationArray()


portAndKeys()
for l in locationID:
    weatherAPIReading = weatherRequest(OWMKey,l)
    ##print(weatherPayload(weatherAPIReading))
    mqttPusher(mqttHost, mqttPort, 'area', weatherPayload(weatherAPIReading))
