#!/bin/sh

export LD_LIBRARY_PATH=/usr/local/lib
mjpg_streamer \
    -i "input_uvc.so -f $IMAGE_FRAMERATE -r $IMAGE_SIZE -d /mnt/video0 -y -n" \
    -o "output_http.so -w /usr/local/www -p $LISTENING_PORT -c $ACCESS_ID:$ACCESS_PWD"