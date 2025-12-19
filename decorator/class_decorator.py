from functools import wraps
import logging
from typing import Callable

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger(object):
    level: logging._Level

    def __init__(self, level: logging._Level = logging.INFO):
        self.level = level

    def __call__(self, func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.logging(result)
        return wrapper

    def logging(self, result):
        logging.log(level=self.level, msg=result)

@Logger()
def funca(n: int):
    return n

funca(1)