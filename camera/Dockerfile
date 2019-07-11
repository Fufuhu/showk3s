FROM debian:buster-slim

# RUN echo "deb http://ftp.jp.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list
RUN apt update && apt install --no-install-recommends -y python3-opencv python3-pip
RUN python3 --version
RUN python3 -c 'import cv2; print(cv2.__version__)'
RUN apt install -y python3-setuptools

# 実行ユーザの準備
RUN useradd django && mkdir -p /home/django && chown -R django:django /home/django
USER django
WORKDIR /home/django
ENV PATH $PATH:/home/django/.local/bin

EXPOSE 8000
COPY --chown=django:django requirements.txt ./
RUN pip3 install --user -r requirements.txt

COPY --chown=django:django project ./
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["python3 manage.py runserver 0.0.0.0:8000"]