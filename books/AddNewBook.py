import boto3
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Books')

title = "Docker"
year = 2019

response = table.put_item(
   Item={
        'year': year,
        'title': title,
        'info': {
            "release_date": "2029-12-01",
            "rank": 5,
            "authors": "Daniel Bruhl"
        }
    }
)

print("Add New Book:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))