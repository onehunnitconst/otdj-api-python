from redis import Redis, ConnectionPool

from settings import get_settings

settings = get_settings()


connection_pool = ConnectionPool(
    host=settings.redis_host, port=settings.redis_port, db=0
)


redis = Redis(connection_pool=connection_pool)


def get_redis_client():
    return redis
