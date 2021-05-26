# unit-grpc-552

Re: https://github.com/nginx/unit/issues/552


## How to Run?

### Server

```bash
cd grpcserver
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.lock.txt
python -m grpcserver.main

> Preparing RPC Service on [::]:49999
> Pinging peers dict_keys([])
```

### Clients

```bash
docker-compose up --build

> unitclient       | 2021/05/26 15:29:21 [info] 11#11 OpenSSL 1.1.1d  10 Sep 2019, 1010104f
> uvicornclient    | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```


## What is there to see?

This may not actually be a bug at all, but rather an "as-designed". When `localhost:9000` and `localhost:9100` are loaded in a browser, we can see in the docker logs that the startup function is run and the two-way RPCs are successful. At the same time, a background task in FastAPI is created which will keep an open channel to the server's response-stream.

With uvicorn, the channel stays open, however, using Unit, the process is destroyed when completed and there is an associated log on the server showing the subscription is closed:

```bash
Pinging peers dict_keys(['ipv4:172.16.239.101:38266', 'ipv4:172.16.239.100:57390'])
2021-05-26 11:30:00,509 - grpc._cython.cygrpc - DEBUG - RPC cancelled for servicer method [/routeguide.RouteGuide/ListFeatures]
Pinging peers dict_keys(['ipv4:172.16.239.101:38266'])
```

## Problem solved

In `config.json`, instead of `processes: {}` - that entire key should be removed so we use 1 static process.