
from turtle import up
import pandas as pd
import requests, json
import csv
from datetime import date

workbook = pd.read_csv('D:/Work/Files/QuadX/Templates/sample_staging.csv')
today = date.today()
with open(f'{today}_created-address-staging-2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['Party ID', 'Line 1', 'Barangay', 'City',  'State', 'Postal Code', 'Country Code', 'Region']
     # write the header
    writer.writerow(header)
    def my_function():
        for index, row in workbook.iterrows():
                url = "https://api.quadx.xyz/v1/locations/provinces/"
                headers = {
                        'Content-Type': 'application/json'
                    }  
                response = requests.get(url, headers=headers)
                data  = json.loads(response.text)

                for province in data['data']:
                    province_name = province['name']
                    region = province['cluster']
                    if province_name.lower() == row['state'].lower():
                        id = province['id']
                        url_city = url + str(id) + '/cities'
                        response_city = requests.get(url_city, headers=headers)
                        data_city  = json.loads(response_city.text)

                        for city in data_city['data']:
                            city_name = city['name']
                            if row['city'].lower() in city_name.lower():
                                city_id = city['id']
                                url_district = 'https://api.quadx.xyz/v1/locations/cities/' + str(city_id) + '/districts'
                                response_district = requests.get(url_district, headers=headers)
                                data_district = json.loads(response_district.text)   

                                for district in data_district['data']:
                                    if (not pd.isna(row['line_2'])):
                                        if row['line_2'] != '.' and district['name'].lower() in row['line_2'].lower():
                                            district_code = district['postal_code']
                                            district_name = district['name']
                                    
                                            update_url = "https://sc-api.shippingcart.com/api/addresses/" + str(row['id']) + "/update"
                                            update_headers = {
                                                    'Connection': 'keep-alive',
                                                    "Accept-Encoding": "*",
                                                    'Content-Type': 'application/json',
                                                    'authorization': 'Bearer {{token}}'
                                                }
                                            payload = {
                                                "data": {
                                                    "party_id": row['party_id'],
                                                    "line_2": district_name,
                                                    "city": city_name,
                                                    "postal_code": district_code,
                                                    "region": region,
                                                    "state": province_name,
                                                    "type": "delivery",
                                                    "country_code": "PH"
                                                }
                                            }
                                            response_update = requests.put(update_url, headers=update_headers, data=json.dumps(payload))
                                            data_update  = json.loads(response_update.text)
                                            # data_csv = [row['party_id'], row['line_1'], district_name, city_name,  province_name, district_code, "PH", region]
                                            data_csv = [data_update['party_id'], data_update['line_1'], data_update['line_2'], data_update['city'],  data_update['state'], data_update['postal_code'], data_update['country_code'], data_update['region']]
                                            print(data_csv)
                                            writer.writerow(data_csv)
    my_function()