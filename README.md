# unit-grpc-552

Re: https://github.com/nginx/unit/issues/552


## How to Run?

`docker-compose up --build`

## What is there to see?

This may not actually be a bug at all, but rather an "as-designed". When `localhost:9000` and `localhost:9100` are loaded, we can see in the docker logs that the startup function is run and the two-way RPCs are successful. At the same time, a background task is created which will keep an open channel to the server's response-stream.

With uvicorn, the channel stays open, however, using Unit, the process is destroyed when completed and there is an associated log on the server showing the subscription is closed:

```bash
Pinging peers dict_keys(['ipv4:172.16.239.101:38266', 'ipv4:172.16.239.100:57390'])
2021-05-26 11:30:00,509 - grpc._cython.cygrpc - DEBUG - RPC cancelled for servicer method [/routeguide.RouteGuide/ListFeatures]
Pinging peers dict_keys(['ipv4:172.16.239.101:38266'])
```
