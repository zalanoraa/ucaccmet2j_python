#part 1
import json
with open('precipitation.json') as file:
    precipitation = json.load(file)
#print(precipitation)

#from csv import DictReader
#with open('stations.csv') as file:
#    reader = DictReader(file)
#    stations = list(reader) 
#print(stations)

seattle_data = []
for data in precipitation:
    if data['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(data)
print(seattle_data)

total_monthly_precipitation=[0] * 12
for data in seattle_data:
    date = data['date']
    date = date.split("-")
    value = data['value']
    total_monthly_precipitation[int(date[1])-1] += value
print(total_monthly_precipitation)



#with open ('results.json', 'w') as f:
#    json.dump ({
#        "Seattle": {
#            "station":"GHCND:US1WAKG0038",
#            "state": "WA",
#            "total_monthly_precipitation": total_monthly_precipitation
#            }
#        }, f, indent=4, sort_keys=True)

#part 2
months_sum = 0
for month in total_monthly_precipitation:
    months_sum += month
total_yearly_precipitation = months_sum
print(total_yearly_precipitation)

relative_monthly_precipitation = []
for month in total_monthly_precipitation:
    relative_monthly_precipitation.append(month/total_yearly_precipitation)
print(relative_monthly_precipitation)


with open ('results.json', 'w') as f:
    json.dump ({
        "Seattle": {
            "station":"GHCND:US1WAKG0038",
            "state": "WA",
            "total_monthly_precipitation": total_monthly_precipitation,
            "total_yearly_precipitation": total_yearly_precipitation,
            "relative_monthly_precipitation": relative_monthly_precipitation,
            }
        }, f, indent=4, sort_keys=True)