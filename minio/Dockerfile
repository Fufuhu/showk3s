# PINE64の場合は、docker buildでOK
# e.g. docker -H pi03.web.ryoma0923.work build -t ~~~~ `pwd`
# Rasbianの入ったRaspberry Piの場合は、
# e.g. docker -H pi02.web.ryoma0923.work build -t fufuhu/minio --build-arg=CPU_ARCH=arm32v7 --build-arg=ARCH=arm `pwd`
# CPU_ARCH、ARM64の場合はarm64v8、ARMv7の場合はarm32v7を指定する
# 起動時
ARG CPU_ARCH=arm64v8
FROM ${CPU_ARCH}/alpine

ENV MINIO_ACCESS_KEY=miniokey
ENV MINIO_SECRET_KEY=miniostorage

# ARCHは、
# x86_64の場合は、amd64を指定する(このファイルでは、FROMの都合上不可)
# ARM64の場合は、arm64
# 32bitのARMの場合はarmを指定する。　
ARG ARCH=arm64
RUN wget https://dl.minio.io/server/minio/release/linux-${ARCH}/minio \
    && chmod 755 minio \
    && mv minio /usr/bin/minio

EXPOSE 9000
ENTRYPOINT ["minio"]
VOLUME ["/export"]
CMD [ "server" ,"--address", "0.0.0.0:9000", "/export" ]