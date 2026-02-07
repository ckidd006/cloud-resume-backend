import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Get current count
        response = table.get_item(Key={'id': 'counter'})
        
        views = 0
        if 'Item' in response and 'views' in response['Item']:
            views = int(response['Item']['views'])
        
        views += 1
        
        # Save updated count
        table.put_item(Item={
            'id': 'counter',
            'views': views
        })
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'views': views})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }