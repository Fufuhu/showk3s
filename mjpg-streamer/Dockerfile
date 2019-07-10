FROM alpine AS downloader
RUN apk add --no-cache git
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git

FROM debian:buster-slim
RUN apt-get update && apt-get install -y libjpeg-dev imagemagick gcc g++ make cmake
COPY --from=downloader mjpg-streamer/mjpg-streamer-experimental ./mjpg-streamer
RUN cd mjpg-streamer && make && make install
RUN cp -pr mjpg-streamer/www /usr/local/www
# mjpg-streamerのリスニングポート
ENV LISTENING_PORT=8080 
# アクセス情報(ユーザID/パスワード)
ENV ACCESS_ID=hoge
ENV ACCESS_PWD=hoge
# 画像のサイズ
ENV IMAGE_SIZE=640x480
# MJPEGのフレームレート
ENV IMAGE_FRAME_RATE=20
COPY start.sh ./
CMD ./start.sh

# docker run -it --rm -p 8080:8080 -v /dev:/mnt --privileged test