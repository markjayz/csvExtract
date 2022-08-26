
from turtle import up
import pandas as pd
import requests, json
import csv
from datetime import date

# prod-data-first-batch
# prod-data-second-batch
# prod-data-third-batch
# prod-data-fourth-batch
# prod-data-fifth-batch
# prod-data-sixth-batch
workbook = pd.read_csv('D:/Work/Files/QuadX/Templates/Update/prod-data-sixth-batch.csv')
today = date.today()

# _created-address-first-batch-prod
# _created-address-second-batch-prod
# _created-address-third-batch-prod
# _created-address-fourth-batch-prod
# _created-address-fifth-batch-prod
# _created-address-sixth-batch-prod
with open(f'{today}_created-address-sixth-batch-prod.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['Party ID', 'Line 1', 'Barangay', 'City',  'State', 'Postal Code', 'Country Code', 'Region']
     # write the header
    writer.writerow(header)
    def my_function():
        for index, row in workbook.iterrows():
            update_url = "https://sc-api.prod.shippingcart.com/api/addresses/" + str(row['id']) + "/update"
            update_headers = {
                    'Connection': 'keep-alive',
                    "Accept-Encoding": "*",
                    'Content-Type': 'application/json',
                    'authorization': 'Bearer {{token}}'
                }
            payload = {
                "data": {
                    "party_id": row['party_id'],
                    "line_2": row['line_2'],
                    "city": row['city'],
                    "postal_code": row['postal_code'],
                    "region": row['region'],
                    "state": row['state'],
                    "type": "row['type]",
                    "country_code": row['country_code']
                }
            }
            response_update = requests.put(update_url, headers=update_headers, data=json.dumps(payload))
            data_update  = json.loads(response_update.text)
            # data_csv = [row['party_id'], row['line_1'], district_name, city_name,  province_name, district_code, "PH", region]
            data_csv = [data_update['party_id'], data_update['line_1'], data_update['line_2'], data_update['city'],  data_update['state'], data_update['postal_code'], data_update['country_code'], data_update['region']]
            print(data_csv)
            writer.writerow(data_csv)
    my_function()