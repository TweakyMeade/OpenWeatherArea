import paho.mqtt.client as mqtt, json, requests 


def portAndKeys():
    global mqttHost
    global mqttPort
    global OWMKey
    with open("appconfig.json") as keyring:
        keyring = json.load(keyring)
        mqttHost = keyring["host"]
        mqttPort = keyring["port"]
        OWMKey = keyring["key"]


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
   
def locationPush(key):
    with open("location.csv") as loc:
       lArray = []
       for id in loc.read().split(','):
            lArray.append(int(id))
    
    for l in lArray:
        mqttPusher(mqttHost, mqttPort, 'area', weatherPayload(weatherRequest(key,l)))

def PrintJSONtoDict(wJSON):
    for a in wJSON:
        print(f"{a}:{wJSON[a]}")

portAndKeys()

PrintJSONtoDict(weatherRequest(OWMKey,3333220))