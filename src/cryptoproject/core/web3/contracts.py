import json
import os

from core.misc.exceptions import NoByteCodeError, NoABIError, BadABIError, NoContractError
from core.misc.loggers import contracts


def load_bytecode(filename: str):
    """
    :param filename: name of the file which contains bytecode of contract
    :raises:
    exceptions.NoByteCodeError
    :return:
    Bytecode of test contract
    """
    if not os.path.isfile(f"{os.path.dirname(__file__)}/contracts/{filename}"):
        raise NoByteCodeError(filename)
    with open(f"{os.path.dirname(__file__)}/contracts/{filename}", "r") as bytecode:
        bytecode = bytecode.read()
        if not bytecode:
            raise NoByteCodeError(filename)
        contracts.debug(f"Successfully loaded bytecode from {filename}")
        return bytecode


def load_abi(filename: str):
    """
    :param filename: name of the file which contains abi of contract ( should be .json )
    :raises:
    exceptions.BadABIError
    exceptions.NoABIError
    :return:
    Dictionary of ABI parameters
    """
    if not filename.endswith(".json"):
        raise BadABIError(filename)
    if not os.path.isfile(f"{os.path.dirname(__file__)}/contracts/{filename}"):
        raise NoABIError(filename)
    with open(f"{os.path.dirname(__file__)}/contracts/{filename}", "r") as abi:
        abi = abi.read()
        if not abi:
            raise NoABIError(filename)
        abi = json.loads(abi)
        if not abi:
            raise NoABIError(filename)
        contracts.debug(f"Successfully loaded ABI from {filename}")
        return abi


def load_contract(contract: str):
    """
    :param contract: folder in <root>/contracts/contracts folder which contains bytecode and abi.json
    :raises:
    exceptions.BadABIError
    exceptions.NoABIError
    exceptions.NoByteCodeError
    exceptions.NoContractError
    :return:
    {"bytecode": <contract bytecode>, "abi": <contract abi>} of test contract
    """
    if not os.path.isdir(f"{os.path.dirname(__file__)}/contracts/{contract}"):
        raise NoContractError(contract)
    return {"bytecode": load_bytecode(f"{contract}/bytecode"), "abi": load_abi(f"{contract}/abi.json")}
