import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Books')

with open("bookdata.json") as json_file:
    books = json.load(json_file, parse_float = decimal.Decimal)
    for book in books:
        year = int(book['year'])
        title = book['title']
        info = book['info']

        print("Add Book:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
