import asyncio
import logging
from core.misc import loggers
from core.web3 import dex, cex
from core.telegram.loggers import TelegramLoggerHandler, TelegramLogger
from core.web3.cex import load_from_env

telegram_logger = TelegramLogger(load_from_env(("BOT_TOKEN", ))["BOT_TOKEN"])
telegram_logger = TelegramLoggerHandler(telegram_logger, [905240578])

logging.basicConfig(level=logging.ERROR)
loggers.credentials.setLevel(logging.INFO)
loggers.contracts.setLevel(logging.INFO)
loggers.dex.setLevel(logging.INFO)
loggers.cex.setLevel(logging.INFO)
loggers.telegram.setLevel(logging.INFO)
loggers.cex.addHandler(telegram_logger)


async def main():
    env = cex.load_from_env(('API_KEY', 'SECRET'))
    mexc = cex.CEX("mexc3", apiKey=env["API_KEY"], secret=env["SECRET"])
    eth_price = await mexc.get_sell_price("ETH/USDT")
    sushiswap = dex.DEX('sushiswap_v2', "arbitrum_one", "a")
    try:
        while True:
            dex_price = await sushiswap.calculate_price("sundae", "weth") * eth_price
            cex_price = (await mexc.get_sell_price("SUNDAE/USDT"))
            if dex_price <= cex_price:
                loggers.cex.info(
                    f"<b>PRICE OF SUNDAE ON DEX HAS BECOME LESS THAN ON CEX")
            loggers.cex.info(f"<b>PRICE OF SUNDAE</b>\n___________\n<b>MEXC</b>: {cex_price}\n<b>SushiSwap</b>: {dex_price}\n")
            await asyncio.sleep(1)
    finally:
        await mexc.close()


if __name__ == '__main__':
    asyncio.run(main())
