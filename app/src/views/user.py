"""Implementation of user API view functions."""

from sqlalchemy import insert, select

from service.db.client import get_session
from service.db.models import User


async def post(body):
    """Writes a new user to the database."""

    username = body["username"]

    sess = get_session()

    stmt = insert(User).values(username=username)
    await sess.execute(stmt)
    await sess.commit()

    return {"username": username}, 200


async def get():
    """Reads all users from the database."""

    sess = get_session()

    stmt = select(User.username)
    result = await sess.execute(stmt)
    result = result.scalars()

    users = list(result)

    return users, 200
