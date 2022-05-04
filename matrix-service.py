
import requests

body = {"locations":[[69.327089, 41.338399],[69.32875921221458, 41.32623097491999]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248f670c64a04ed40d89b0b06fc6313f134',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/matrix/driving-car', json=body, headers=headers)

print(call.status_code, call.reason)
print(call.text)


file1 = open("/home/jamshid/Documents/python/openroute/json.txt","w")
L = [call.text]   
file1.writelines(L)
file1.close() 