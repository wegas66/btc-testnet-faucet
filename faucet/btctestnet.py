import os
from pycoin.symbols.xtn import network
from pycoin.coins.tx_utils import create_signed_tx
from pycoin.services import spendables_for_address
# from pycoin.services.blockcypher import BlockcypherProvider
from .NewBlockcypher import NewBlockcypherProvider
from pycoin.networks.default import set_default_netcode
from dotenv import load_dotenv

load_dotenv()
set_default_netcode('XTN')

TX_SUM = 10000
FEE = 60000
MY_ADDRESS = os.getenv('MY_ADDRESS')
MY_WIF = os.getenv('MY_WIF')
MY_ADDRESS_2 = os.getenv('MY_ADDRESS_2')
MY_WIF_2 = os.getenv('MY_WIF_2')

ADDRESSES = [{'address': MY_ADDRESS, 'wif': MY_WIF}, {'address': MY_ADDRESS_2, 'wif': MY_WIF_2}]

provider = NewBlockcypherProvider()


def send_tx(address_out: str) -> str:
    for address in ADDRESSES:
        spendables = provider.spendables_for_address(address['address'])
        if len(spendables) == 0:
            continue
        balance = sum([s.coin_value for s in spendables])
        remain = balance - TX_SUM - FEE
        tx = create_signed_tx(network, spendables, [(address_out, TX_SUM), (address['address'], remain)], wifs=[address['wif']], fee=FEE)
        result = provider.broadcast_tx(tx)
        return result['tx']['hash']
    raise Exception('Transaction blocked')

