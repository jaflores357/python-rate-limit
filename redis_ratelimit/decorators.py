from functools import wraps
from time import sleep
from redis_ratelimit.exceptions import RateLimited
from redis_ratelimit.utils import is_rate_limited


def ratelimit(rate, key, redis_url='redis://localhost:6379/0'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            while is_rate_limited(rate, key, f, redis_url):
                sleep(0.2)     
            return f(*args, **kwargs)
        return decorated_function
    return decorator
