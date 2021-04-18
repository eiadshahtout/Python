import requests

url = "https://api.weatherapi.com/v1/current.json?key=d14bb1b4b449419aa0a214517211804&q=London&aqi=no"
r = requests.get(url)
print(f"Status code {r.status_code}")

response_dicts = r.json()
print(response_dicts)
print("-" * 50)
print(f"Full_info: {response_dicts['location']}")

print("-" * 50)
new_response = response_dicts['location']
print(f"Name: {new_response['name']}")

current_time = response_dicts['current']
print("-" * 50)
print(f"Current Time: {current_time['last_updated']}")
