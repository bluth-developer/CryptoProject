from core.misc import loggers
from core.misc.exceptions import NotSupportedTokensChainError, NotSupportedTokenError

tokens = {
    "arbitrum_one": {
        "sundae": "0x352F4bF396a7353A0877f99e99757E5d294Df374",
        "weth": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
    }
}


def get_address(token: str, chain: str):
    loggers.dex.debug(f"Loading token \"{token}\" in the chain \"{chain}\"")
    chain_tokens = tokens.get(chain)
    if not chain_tokens:
        raise NotSupportedTokensChainError(chain)
    address = chain_tokens.get(token)
    if not address:
        raise NotSupportedTokenError(token, chain)
    loggers.dex.debug(f"Address of token \"{token}\" in the chain \"{chain}\" is {address}")
    return address

