from dataclasses import dataclass


@dataclass
class ERC20:
    abi: str = open('./assets/abi/erc20.json', 'r').read()


@dataclass
class USABasketballData:
    address: str = '0x2aa80a13395425EF3897c9684a0249a5226eA779'
    abi: str = open('./assets/abi/basketball.json', 'r').read()


@dataclass
class MisterMigglesData:
    address: str = '0x1aeD60A97192157fDA7fb26267A439d523d09c5e'
    abi: str = open('./assets/abi/miggles.json', 'r').read()


@dataclass
class EthEtfData:
    address: str = '0xb5408b7126142C61f509046868B1273F96191b6d'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class ToshiData:
    address: str = '0xE65dFa5C8B531544b5Ae4960AE0345456D87A47D'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class EURCData:
    address: str = '0x615194d9695d0c02Fc30a897F8dA92E17403D61B'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class TreasureChestData:
    address: str = '0x2E2c0753fc81BE22381c674ADD7A05F24cfD9761'
    abi: str = open('./assets/abi/treasure_chest.json', 'r').read()


@dataclass
class LiquidData:
    address: str = '0x1b9Ac8580d2E81d7322f163362831448E7FcAD1B'
    abi: str = open('./assets/abi/mint_fun.json', 'r').read()


@dataclass
class ETHCantBeStoppedData:
    address: str = '0xb0FF351AD7b538452306d74fB7767EC019Fa10CF'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class BuildathonData:
    address: str = '0x1aeD60A97192157fDA7fb26267A439d523d09c5e'
    abi: str = open('./assets/abi/miggles.json', 'r').read()


@dataclass
class HappyNouniversaryData:
    address: str = '0xE0fE6DD851187c62a79D00a211953Fe3B5Cec7FE'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class PoolTogetherData:
    address: str = '0x0d7D21Ae700D0e3d9f320A26b4fF23F314F6d8C8'
    abi: str = open('./assets/abi/pool_together.json', 'r').read()


@dataclass
class StixLaunchData:
    address: str = '0xa7891c87933BB99Db006b60D8Cb7cf68141B492f'
    abi: str = open('./assets/abi/mint_fun.json', 'r').read()


@dataclass
class TheWorldAfterEthEtfApprovalData:
    address: str = '0x955FdFdFd783C89Beb54c85f0a97F0904D85B86C'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class ETFEREUMData:
    address: str = '0xE8aD8b2c5Ec79d4735026f95Ba7C10DCB0D3732B'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class EthereumETFData:
    address: str = '0xC00F7096357f09d9f5FE335CFD15065326229F66'
    abi: str = open('./assets/abi/eth_etf.json', 'r').read()


@dataclass
class IntroducingCoinbaseWalletWebAppData:
    address: str = '0x6B033e8199ce2E924813568B716378aA440F4C67'
    abi: str = open('./assets/abi/mint_fun.json', 'r').read()


@dataclass
class JuicyAdventureData:
    address: str = '0x6ba5Ba71810c1196f20123B57B66C9ed2A5dBd76'
    abi: str = open('./assets/abi/juicy_adventure.json', 'r').read()


@dataclass
class ForbesData:
    address: str = '0x0821D16eCb68FA7C623f0cD7c83C8D5Bd80bd822'
    abi: str = open('./assets/abi/mint_fun.json', 'r').read()