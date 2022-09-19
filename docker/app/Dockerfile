FROM python:3.9.13-alpine3.16

COPY ./ /app/
COPY ./docker/app/supervisord.conf /etc/supervisord.conf

RUN apk add build-base postgresql-dev \
  && python3 -m venv /env \
  && /env/bin/pip3 install --upgrade pip \
  && /env/bin/pip3 install --no-cache-dir -r /app/requirements.txt \
  && /env/bin/pip3 install supervisor  

WORKDIR /app
RUN mkdir /var/log/celery

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

# CMD ["supervisord", "-c", "/etc/supervisord.conf"]
ENTRYPOINT [ "./docker-entrypoint.sh" ]