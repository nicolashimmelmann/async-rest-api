"""The main module of the API"""

import contextlib
from pathlib import Path

from connexion import AsyncApp
from connexion.middleware import MiddlewarePosition

from service.db import client
from db_session_middleware import DatabaseSessionMiddleware


@contextlib.asynccontextmanager
async def lifespan(_):
    """Use the Starlette lifespan to init the tables."""

    # Any code to run on startup
    await client.init_tables()

    yield

    # Any code to run on teardown


app = AsyncApp(__name__, specification_dir="spec", lifespan=lifespan)
app.add_api("v1.yaml", strict_validation=True)

# Apply the custom db session middleware
app.add_middleware(
    DatabaseSessionMiddleware,
    MiddlewarePosition.BEFORE_SECURITY,
)


# Only for development. In production, a proper ASGI server is needed.
if __name__ == "__main__":
    app.run(
        f"{Path(__file__).stem}:app",
        port=8080,
        host="0.0.0.0",
    )
