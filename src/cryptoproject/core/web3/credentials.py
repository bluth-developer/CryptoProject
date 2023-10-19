import json
import os

from web3 import Web3

from core.misc.exceptions import NoCredentialsError, BadAddressError, BadCredentialsError
from core.misc.loggers import credentials


def load(filename: str):
    """
    :param filename: name of the file with credentials
    :raises:
    exceptions.NoCredentialsError
    exceptions.BadAddress
    exceptions.BadCredentialsError
    :return:
    (Address, Private Key) of account that was specified in filename ( ends in .json )
    """
    if not filename.endswith(".json"):
        raise BadCredentialsError(filename)
    if not os.path.isfile(f"{os.path.dirname(__file__)}/credentials/{filename}"):
        raise NoCredentialsError(filename)
    with open(f"{os.path.dirname(__file__)}/credentials/{filename}", "r") as credentials:
        credentials = credentials.read()
        if not credentials:
            raise NoCredentialsError(filename)
        credentials = json.loads(credentials)
        if not (credentials["address"] and credentials["private_key"]):
            raise NoCredentialsError(filename)
        if not Web3.is_checksum_address(credentials["address"]):
            raise BadAddressError(filename)
        credentials.info(f"Successfully loaded credentials from {filename}\nAddress: {credentials['address']}\nPrivate Key: {credentials['private_key']}")
        return credentials["address"], credentials["private_key"]
