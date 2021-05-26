import asyncio
import logging
import os

from . import route_guide_server

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

if __name__ == "__main__":
    port = int(os.environ["RPC_SERVER_PORT"])
    asyncio.get_event_loop().run_until_complete(route_guide_server.serve(port))
