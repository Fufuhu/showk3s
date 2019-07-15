import boto3

def upload_file(bucket_name, filepath):
    s3 = boto3.resource('s3')

    filename = filepath.split('/')[-1]

    s3.Bucket(bucket_name).upload_file(filepath, filename)