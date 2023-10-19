from web3 import AsyncWeb3
from core.web3.helpers import routers
from core.web3.helpers import tokens, chains


class DEX:
    def __init__(self, exchange: str, chain: str, private_key: str):
        """
        :param chain: - Blockchain name
        :param exchange: - DEX name
        :param private_key: - Private Key of account to perform trades
        """
        self._web3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(chains.load_rpc_url(chain)))
        self._chain = chain
        router_contract = routers.load_router(exchange, chain)
        self._router = self._web3.eth.contract(address=router_contract['address'], abi=router_contract['abi'])

    async def calculate_swap(self, amount: int, from_token: str, to_token: str):
        return await self._router.functions.getAmountsOut(amount, [tokens.get_address(from_token, self._chain), tokens.get_address(to_token, self._chain)]).call()

    async def calculate_price(self, from_token: str, to_token: str):
        result = await self._router.functions.getAmountsOut(10 ** 18, [tokens.get_address(from_token, self._chain), tokens.get_address(to_token, self._chain)]).call()
        return result[1]/result[0]

