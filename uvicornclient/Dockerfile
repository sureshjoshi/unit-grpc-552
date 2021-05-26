FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.lock.txt
CMD ["uvicorn", "--log-level", "debug", "--host", "0.0.0.0", "--port", "80", "uvicornclient.main:app"]