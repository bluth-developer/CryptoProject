from core.misc import loggers
from core.misc.exceptions import NotSupportedChainError

chains = {
    "goerli": "https://goerli.infura.io/v3/8031bb68ecca4ea0aa983c2059c32d50",
    "arbitrum_one": "https://arbitrum-mainnet.infura.io/v3/8031bb68ecca4ea0aa983c2059c32d50"
}


def load_rpc_url(chain: str):
    """
    :param chain: - Blockchain name
    :return:
    JSON RPC url to connect to the blockchain
    """
    loggers.dex.debug(f"Loading chain \"{chain}\"")
    rpc_url = chains.get(chain)
    if not rpc_url:
        raise NotSupportedChainError(chain)
    return rpc_url




