
from turtle import up
import pandas as pd
import requests, json
import csv
import config
from datetime import date

today = date.today()
workbook = pd.read_csv(f'input/vistra/vistra-data.csv')
with open(f'output/{today}_vistra_response.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['TrackingNumber', 'Payload', 'Response']
     # write the header
    writer.writerow(header)
    def my_function():
        for index, row in workbook.iterrows():
            vistra_url = config.VISTRA_URL
            update_headers = {
                    'Connection': 'keep-alive',
                    "Accept-Encoding": "*",
                    'Content-Type': 'application/json',
                    'authorization': "Bearer " + config.VISTRA_TOKEN
                }
            payload = {
                "Tracking": row['Tracking'],
                "TransactionDate": row['TransactionDate'],
                "ReferenceNumber": row['ReferenceNumber'],
                "Product": row['Product'],
                "CustomerID": row['CustomerID'],
                "Consignee_Name": row['Consignee_Name'],
                "Consignee_Address1": row['Consignee_Address1'],
                "Consignee_Address2": row['Consignee_Address2'],
                "Consignee_Barangay": row['Consignee_Barangay'],
                "Consignee_City": row['Consignee_City'],
                "Consignee_Province": row['Consignee_Province'],
                "Consignee_ZipCode": row['Consignee_ZipCode'],
                "Consignee_Phone": row['Consignee_Phone'],
                "Consignee_CellNo": row['Consignee_CellNo'],
                "BoxSize": row['BoxSize'],
                "DeliveryType": row['DeliveryType'],
                "Weight": row['Weight'],
            }
            response = requests.post(vistra_url, headers=update_headers, data=json.dumps(payload))
            data_csv = [row['Tracking'], json.dumps(payload), response.text]
            print(response.text)
            writer.writerow(data_csv)
    my_function()