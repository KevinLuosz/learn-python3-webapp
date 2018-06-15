import orm
from models import User, Blog, Comment
import asyncio



async def test(loop):
    await  orm.create_pool(loop, user='root', password='password', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    await orm.destroypool()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
