import openrouteservice 
from openrouteservice.distance_matrix import distance_matrix

coords = ((69.327089, 41.338399),(69.32875921221458, 41.32623097491999))
key="5b3ce3597851110001cf6248f670c64a04ed40d89b0b06fc6313f134"

client = openrouteservice.Client(key=key) # Specify your personal API key
distance = distance_matrix(client, coords, profile='driving-car') 

print(distance)