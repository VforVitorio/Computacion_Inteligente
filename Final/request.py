import requests
import api_keys as api

# Use your actual API key

url = f"https://servizos.meteogalicia.gal/apiv4/getSolarInfo?coords=-8.350573861318628,43.3697102138535&API_KEY={api.API_KEY}"

response = requests.get(url)
print(response.json())


if response.status_code == 200:
    data = response.json()
    # print(data)

else:
    print("Error al hacer la solicitud:", response.status_code)
