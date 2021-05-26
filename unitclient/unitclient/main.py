import asyncio
import os

import grpc
from fastapi import FastAPI


from . import route_guide_client, route_guide_pb2_grpc


app = FastAPI(
    title="Unit GRPC Client",
)

async def receive_ping():
    print("-------------- UNARY-STREAM - ListFeatures --------------")
    url = os.environ["RPC_SERVER_URL"]
    async with grpc.aio.insecure_channel(url) as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        await route_guide_client.guide_list_features(stub)

@app.on_event("startup")
async def startup_event():
    print("Running startup_event_handler")
    url = os.environ["RPC_SERVER_URL"]
    async with grpc.aio.insecure_channel(url) as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- UNARY-UNARY - GetFeature --------------")
        await route_guide_client.guide_get_feature(stub)
        print("-------------- STREAM-UNARY - RecordRoute --------------")
        await route_guide_client.guide_record_route(stub)
        print("-------------- STREAM-STREAM - RouteChat --------------")
        await route_guide_client.guide_route_chat(stub)

    asyncio.get_event_loop().create_task(receive_ping())

@app.get("/")
async def root():
    return {"status": "unitclient is running"}
