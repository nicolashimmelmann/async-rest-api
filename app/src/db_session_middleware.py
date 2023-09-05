from starlette.types import ASGIApp, Receive, Scope, Send

from service.db import client as db_client


class DatabaseSessionMiddleware:
    """A custom middleware which creates a database session on each request."""

    def __init__(self, next_app: ASGIApp):
        self.next_app = next_app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        """Uses the db client to create a new session and assigns it to the
        context variable so that it is accessible in the views for the current
        request."""

        async with db_client.async_session() as session:
            db_client.db_session_context.set(session)
            # Run next middleware
            await self.next_app(scope, receive, send)
