import pandas as pd
import requests

df = pd.read_csv('data.csv')
locations = df['Locations/Villages'].dropna().tolist()
api_key = '9A9Rw2AFNBATbbZ8RDiqiuishlPFY1tj'
"""
Edit the name of the csv file you are passing as input and name the corresponding output file
within the open() function to avoid confusion (not necessary)
If you encounter any bugs, problems feel free to reach out to me!!

Kind Regards,
Kausik D
"""
with open('bngwest.txt','w') as file:
    for i in locations:
        response = requests.get(f"https://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={i}")
        if response:
            data = response.json()
            latitude = data['results'][0]['locations'][0]['latLng']['lat']
            longitude = data['results'][0]['locations'][0]['latLng']['lng']
            file.writelines(f"{i},{latitude},{longitude}\n")
        else:
            pass
    file.close()
