import logging

from web3 import Web3
from core.web3.helpers import chains
from core.credentials import load
from core.web3.contracts import load_contract
from core.misc.loggers import credentials, contracts


logging.basicConfig(level=logging.ERROR)
credentials.setLevel(logging.INFO)
contracts.setLevel(logging.DEBUG)


web3 = Web3(Web3.HTTPProvider(chains.goerli))
address, private_key = load("main.json")

contract = load_contract("1158")
contract = web3.eth.contract(abi=contract["abi"], bytecode=contract["bytecode"])


constructor = contract.constructor().build_transaction(
    {
        'from': Web3.to_checksum_address(address),
        'nonce': web3.eth.get_transaction_count(Web3.to_checksum_address(address)),
    }
)
tx = web3.eth.account.sign_transaction(constructor, private_key)
tx_hash = web3.eth.send_raw_transaction(tx.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')

