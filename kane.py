import boto3
dynamodb = boto3.resource('dynamodb',
	aws_access_key_id = '',
	aws_secret_access_key = '',
	region_name ="ap-south-1"
	)
table_name = 'jayanth'
item = {
   'course' : 'cloud computing and big data'
}
try:
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)
    print(f"add items to '{table_name}': {item}")
except Exception as e:
    print(f"An error occured as: {e}")
