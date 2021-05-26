FROM nginx/unit:1.23.0-python3.9
WORKDIR /app
COPY ./config.json /docker-entrypoint.d/config.json
COPY . /app
RUN pip install -r requirements.lock.txt
