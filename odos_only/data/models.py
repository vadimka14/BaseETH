import json
from dataclasses import dataclass

from libs.eth_async.utils.files import read_json
from libs.eth_async.classes import AutoRepr, Singleton
from libs.eth_async.data.models import RawContract, DefaultABIs

from data.config import ABIS_DIR


class Contracts(Singleton):
    WETH = RawContract(
        title='ETH',
        address='0x4200000000000000000000000000000000000006',
        abi=read_json(path=(ABIS_DIR, 'WETH.json'))
    )
    USDC = RawContract(
        title='USDC',
        address='0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913',
        abi=DefaultABIs.Token
    )

    ODOS = RawContract(
        title='odos',
        address='0x19cEeAd7105607Cd444F5ad10dd51356436095a1',

        abi=read_json(path=(ABIS_DIR, 'odos.json'))
    )




