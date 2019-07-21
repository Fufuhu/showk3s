#! /bin/sh

# ENDPOINT_URL='http://pi03.web.ryoma0923.work:9000'
# BUCKET_NAME='showks'
# export AWS_ACCESS_KEY_ID='miniokey'
# export AWS_SECRET_ACCESS_KEY='miniostorage'

echo "ENDPOINT URL:" $ENDPOINT_URL
echo "BUCKET NAME:" $BUCKET_NAME

while :
do

aws --endpoint-url $ENDPOINT_URL s3 sync s3://$BUCKET_NAME ./images
sleep 300

done showks