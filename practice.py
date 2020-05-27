import json
import boto3
import pytz
import base64

s3=boto3.client('s3')

def lambda_handler(event, context):
    fileContent = base64.b64decode(inputPayload['content'])
    input = s3.get_object(Bucket="inputjpgimg", key="jpg_44.jpg")

    im = Image.open(input)
    im.save('output.webp')

    local_file_name = 'tmp/' + "output.webp"
    s3.put_object(Bucket="outputwebp",key="output.webp")


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }