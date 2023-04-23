import opencage.geocoder
import pandas as pd

df = pd.read_csv('bngeast.csv')
locations = df['Locations/Villages'].dropna().tolist()
#print(locations)
api_key = '8685f84780a44bf894550f98cd7c0344'

geocoder = opencage.geocoder.OpenCageGeocode(api_key)
"""
Edit the name of the csv file you are passing as input and name the corresponding output file
within the open() function to avoid confusion (not necessary)
If you encounter any bugs, problems feel free to reach out to me!!

Kind Regards,
Kausik D
"""
with open('bngeast.txt','w') as file:
    for location in locations:
        results = geocoder.geocode(location)
        # print(results)
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            write = f"{location},{lat},{lng}"
            file.write(f"{write}\n")
        else:
            pass
file.close()
