FROM python:3.7-alpine

RUN pip install awscli
ENV AWS_ACCESS_KEY_ID dummy
ENV AWS_SECRET_ACCESS_KEY dummy
ENV BUCKET_NAME showks
ENV ENDPOINT_URL http://pi03.web.ryoma0923.work:9000
COPY src ./
CMD ["/bin/sh", "s3_sync_with_loop.sh"]