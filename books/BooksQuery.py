import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Books')

print("Books From 2023")

response = table.query(
    KeyConditionExpression=Key('year').eq(2023)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])