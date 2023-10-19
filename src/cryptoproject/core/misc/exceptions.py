# Contracts errors

class NoByteCodeError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"No bytecode was found in <root>/core/contracts/{filename}")


class NoABIError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"No Contract ABI was found in <root>/core/contracts/{filename}")


class BadABIError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"Contract ABI must be .json file ( current file is <root>/core/contracts/{filename} )")


class NoContractError(Exception):
    def __init__(self, contract: str):
        self.contract = contract
        super().__init__(f"No Contract Folder <{contract}> found in <root>/core/contracts/")


# Credentials errors

class NoCredentialsError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"No credentials was found in <root>/core/credentials/{filename}")


class BadAddressError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"Bad address was specified in <root>/core/credentials/{filename}")


class BadCredentialsError(Exception):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"Credentials must be .json file ( current file is <root>/core/credentials/{filename} )")


# CEX errors

class NoEnvKeysError(Exception):
    def __init__(self, key: str):
        self.key = key
        super().__init__(f"Key \"{key}\" couldn't be found in the .env")


# DEX errors

class NotSupportedDEXError(Exception):
    def __init__(self, exchange: str):
        self.exchange = exchange
        super().__init__(f"DEX \"{exchange}\" is not supported")


class NotSupportedChainDEXError(Exception):
    def __init__(self, exchange: str, chain: str):
        self.exchange = exchange
        self.chain = chain
        super().__init__(f"DEX \"{exchange}\" is not supported in the chain \"{chain}\"")


class NotSupportedChainError(Exception):
    def __init__(self, chain: str):
        self.chain = chain
        super().__init__(f"Chain \"{chain}\" is not supported")


class NotSupportedTokenError(Exception):
    def __init__(self, token: str, chain: str):
        self.token = token
        self.chain = chain
        super().__init__(f"Token \"{token}\" is not supported in the chain \"{chain}\"")


class NotSupportedTokensChainError(Exception):
    def __init__(self, chain: str):
        self.chain = chain
        super().__init__(f"Tokens in chain \"{chain}\" are not supported")


# Telegram Logger errors

class SendingProcessNotStartedError(Exception):
    def __init__(self):
        super().__init__(f"Process that sends messages hasn't been started yet")
