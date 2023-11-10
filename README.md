# OpenWeatherArea
This project is using OpenWeatherMap's API to record multiple weather report to ultimately injected them to a local Database,
I am currently using INFLUX2,

Python code is transmits to a mosquitto mqtt broker, Configured by Node-red to attach Measurement of the location an remove it from json, then sent directly to influx2

I have API Key, Host name and port numbers saved in a .env file. Location ID will be sorted in a csv file, 
List of ID found in city.list.json.gz in http://bulk.openweathermap.org/sample
