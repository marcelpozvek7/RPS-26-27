import requests 
url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m"

klic = requests.get(url)

klicJSON = klic.json()

print(klicJSON["current"]["temperature_2m"])
