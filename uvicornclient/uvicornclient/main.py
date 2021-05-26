import os

import grpc
from fastapi import FastAPI, Request

from . import route_guide_pb2_grpc, route_guide_client


app = FastAPI(
    title="Uvicorn GRPC Client",
)


@app.on_event("startup")
async def startup_event():
    url = os.environ["RPC_SERVER_URL"]
    async with grpc.aio.insecure_channel(url) as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- UNARY-UNARY - GetFeature --------------")
        await route_guide_client.guide_get_feature(stub)
        print("-------------- UNARY-STREAM - ListFeatures --------------")
        await route_guide_client.guide_list_features(stub)
        print("-------------- STREAM-UNARY - RecordRoute --------------")
        await route_guide_client.guide_record_route(stub)
        print("-------------- STREAM-STREAM - RouteChat --------------")
        await route_guide_client.guide_route_chat(stub)


@app.get("/")
async def root():
    return {"status": "uvicornclient is running"}
