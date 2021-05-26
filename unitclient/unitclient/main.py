import asyncio
import logging
import os

import grpc
from fastapi import FastAPI


from . import route_guide_client, route_guide_pb2_grpc

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)

task = None

app = FastAPI(
    title="Unit GRPC Client",
)


async def receive_ping():
    logger.info("-------------- UNARY-STREAM - ListFeatures --------------")
    url = os.environ["RPC_SERVER_URL"]
    async with grpc.aio.insecure_channel(url) as channel:
        logger.info("In receive_ping channel")
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        await route_guide_client.guide_list_features(stub)


@app.on_event("startup")
async def startup_event():
    logger.info("Running startup_event_handler")
    url = os.environ["RPC_SERVER_URL"]
    async with grpc.aio.insecure_channel(url) as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        logger.info("-------------- UNARY-UNARY - GetFeature --------------")
        await route_guide_client.guide_get_feature(stub)
        logger.info("-------------- STREAM-UNARY - RecordRoute --------------")
        await route_guide_client.guide_record_route(stub)
        logger.info("-------------- STREAM-STREAM - RouteChat --------------")
        await route_guide_client.guide_route_chat(stub)

    global task
    task = asyncio.get_event_loop().create_task(receive_ping())


@app.get("/")
async def root():
    global task
    return {"status": f"unitclient is running {task}"}
