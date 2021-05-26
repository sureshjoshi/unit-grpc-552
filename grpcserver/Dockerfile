FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.lock.txt
CMD ["python", "-m", "grpcserver.main"]