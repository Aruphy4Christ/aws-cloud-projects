
import boto3
import datetime
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'rufus-backups-2026'
FOLDER_TO_BACKUP = '/home/ubuntu/myfiles'

today = datetime.datetime.now().strftime('%Y-%m-%d')

for filename in os.listdir(FOLDER_TO_BACKUP):
    filepath = os.path.join(FOLDER_TO_BACKUP, filename)
    s3_key = f'backups/{today}/{filename}'
    s3.upload_file(filepath, BUCKET_NAME, s3_key)
    print(f'Uploaded {filename} to S3!')

print('Backup complete!')


