import os
import sys
import uuid
import json
import boto3
from PIL import Image
import PIL.Image


s3_client = boto3.client('s3')

'''def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)'''

def converted_image(image_path, converted_path):
    with Image.open(image_path) as image:
        Image.save(format="webp")
        image.save(converted_path)


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/converted-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        converted_image(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}-converted'.format(bucket), key)

'''
def lambda_handler(event, context):
    # TODO implement
    print(event)
    s3 = boto3.client('s3')
    input_obj = s3.get_object(Bucket='inputjpgimg', key='jpg_44.jpg')

    im = Image.open(input_obj)
    output = im.save('output.webp')
    # output_obj=s3.put_object(Bucket="outputwebp",key='output.webp',body="output.webp","rb").read())

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
'''

# m = img.imread(file_content)
# img.imsave('cropped.webp', m)
local_file_name = 'tmp/' + "inputjpg.jpg"
s3.Bucket("inputjpgimg").download_file("inputjpg.jpg", local_file_name)
# s3.download_file(Your_bucket_name, Your_key_name, Your_file_name)

# s3.download_file(bucket="inputjpgimg",key="jpg_44.jpg",'/temp/file.jpg')

# s3.put_object(Bucket='outputwebp', key='output.webp',Body=open("output.webp","rb").read())
s3.upload_file(local_file_name, "outputwebp", "output.webp")