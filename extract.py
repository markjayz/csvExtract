
import pandas as pd
import requests, json
import csv
from datetime import date

workbook = pd.read_excel('/Users/markjaysonlomboy/Desktop/SC-BULK-TEST.xlsx')
today = date.today()
with open(f'{today}_created-orders.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['Tracking Number',  'Buyer Name', 'Description', 'Print Label']
     # write the header
    writer.writerow(header)
    def my_function():
        for index, row in workbook.iterrows():
                url = "{{endpoint_url}}}"
                payload={
                        "currency":"USD",
                        "total":"0.00",
                        "status":"for_acceptance",
                        "payment_method":"other",
                        "payment_provider":"other",
                        "buyer_name":row['Recipient Name'],
                        "shipment":"au-air",
                        "email":"customercare@shippingcart.com",
                        "declared_value":row['Declared Value'],
                        "parcel":{
                            "dimensions":{
                                "length":row['Length'],
                                "width":row['Width'],
                                "height":row['Height'],
                                "uom":"cm"
                            },
                            "weight":{
                                "value":row['Weight'],
                                "uom":"kg"
                            }
                        },
                        "metadata":None,
                        "pickup_address":{
                            "title":None,
                            "name":"Natonic",
                            "company":"Natonic",
                            "code":None,
                            "phone_number":"+61-408-088617",
                            "mobile_number":"+61-408-088617",
                            "fax_number":None,
                            "email":None,
                            "line_1":"Shop 1, 243 Forest Rd ",
                            "line_2":"",
                            "district":"",
                            "city":"Hurtsville",
                            "state":"NSW",
                            "country":"AU",
                            "postal_code":"2220",
                            "remarks":"AU Warehouse Address"
                        },
                        "delivery_address":{
                            "title":None,
                            "name":row['Recipient Name'],
                            "company":None,
                            "code":None,
                            "phone_number":row['Contact Number'],
                            "mobile_number":row['Contact Number'],
                            "fax_number":None,
                            "email":None,
                            "line_1":row['Street Address'],
                            "line_2":"",
                            "district":row['Barangay'],
                            "city":row['City / Municipality'],
                            "state":row['Province'],
                            "country":"PH",
                            "postal_code":row['Postal Code'],
                            "remarks":row['Landmarks, Floor or Unit Number']
                        },
                        "return_address": {
                             "title":None,
                            "name":"Natonic",
                            "company":"Natonic",
                            "code":None,
                            "phone_number":"+61-408-088617",
                            "mobile_number":"+61-408-088617",
                            "fax_number":None,
                            "email":None,
                            "line_1":"Shop 1, 243 Forest Rd ",
                            "line_2":"",
                            "district":"",
                            "city":"Hurtsville",
                            "state":"NSW",
                            "country":"AU",
                            "postal_code":"2220",
                            "remarks":"AU Warehouse Address"
                        },
                        "preferred_pickup_time":"",
                        "preferred_delivery_time":"",
                        "contact_number":"",
                        "items":[
                            {
                                "type":"product",
                                "description":row['Item Description'],
                                "amount":row['Declared Value'],
                                "quantity":1,
                            }
                        ]
                        } 
                headers = {
                                'Content-Type': 'application/json',
                                'authorization': 'Bearer {{token}}'
                            }
                print('>>> Create Order') 
                response = requests.post(url, headers=headers, data=json.dumps(payload))
                #print(response.text , response.status_code)
            
                data  = json.loads(response.text)
                trackingNumber = data['tracking_number']
                print('Created:' + data['tracking_number']) 
                label = requests.get('https://fjl88r5bx4.execute-api.ap-southeast-1.amazonaws.com/staging/print/' + trackingNumber + '?type=zebra')
                ggxlabel = json.loads(label.text)
                awb = ggxlabel['message']['awb']
                data = [data['tracking_number'], row['Recipient Name'],  row['Item Description'], awb]
                # write the data
                writer.writerow(data)
    my_function()

