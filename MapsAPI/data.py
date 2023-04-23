import pandas as pd

df = pd.read_csv('bngeast.csv')
locations = df['Locations/Villages'].tolist()
# print(locations)

# with open('bngeast.txt','w') as file:
#     for i in locations:
#         file.writelines(f"{i}\n")
# file.close()
