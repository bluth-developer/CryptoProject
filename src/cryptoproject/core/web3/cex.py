from os import environ

import ccxt.async_support as ccxt
from dotenv import find_dotenv, load_dotenv

from core.misc.exceptions import NoEnvKeysError
from core.misc import loggers


class CEX:
    """
    Implements fast operations with CEXes
    """
    def __init__(self, exchange: str, *args, **kwargs):
        """
        :param exchange: - Name of exchange (listed in ccxt)
        :param args:
        :param kwargs: - kwargs
        """
        self._exchange: ccxt.Exchange = getattr(ccxt, exchange)(kwargs)

    async def get_sell_price(self, pair):
        """
        :return:
        Price at which the pair can be sold
        """
        return (await self._exchange.fetch_order_book(pair))["bids"][0][0]

    async def close(self):
        await self._exchange.close()


def load_from_env(keys: tuple):
    """
    :param keys: Keys to load
    :return:
    Keys loaded from .env
    For example apiKey, secret
    """
    loggers.cex.debug(f"Loading {keys} from .env")
    load_dotenv(find_dotenv())
    for key in keys:
        if not environ.get(key):
            raise NoEnvKeysError(key)
    return {key: environ.get(key) for key in keys}


