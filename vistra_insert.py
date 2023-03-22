
from turtle import up
import pandas as pd
import requests, json
import csv
from datetime import date

workbook = pd.read_csv('C:/Users/John Richard/Project/csvExtract/input/vistra-extract.csv')
today = date.today()
with open(f'output/{today}_vistra_payload.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['TrackingNumber', 'Payload']
     # write the header
    writer.writerow(header)
    def my_function():
        for index, row in workbook.iterrows():
            vistra_url = "https://appsvc.azurewebsites.net/wmsapi/api/ShippingCart/InsertOrder"
            update_headers = {
                    'Connection': 'keep-alive',
                    "Accept-Encoding": "*",
                    'Content-Type': 'application/json',
                    'authorization': 'Bearer DJkzHFXSdIZWK23mRJjaY9O5X5EvyqPiqvvDtAYztcgHsO0dWDN_5oBBNlH6H9OmGPRVR7v9lsF_PaYaGCSHF7jGWsI_T-XfWBoZUd8X3biRVfW6CCemsNvJ0oJhLP9p5wvFJuW1X0DKZlnvY3gx2Kfp93heRV0gazVSJPBx_AcLIqoPUthQjAQiTTTZgax91jY2nuLvKWe33VQDmjwJow'
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
            data_csv = [row['Tracking'], json.dumps(payload)]
            print(response.text)
            writer.writerow(data_csv)
    my_function()