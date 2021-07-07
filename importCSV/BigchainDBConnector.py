from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit


def sendTransatcionToBigChainDB(assetdata):
    assetdata_tx = {'data': { +assetdata+},}
    print(assetdata)
    alice = generate_keypair()
    bdb_root_url = 'http://59.0.198.238:9984'  # Use YOUR BigchainDB Root URL here
    bdb = BigchainDB(bdb_root_url)
    asset_metadata = {"Survey Type": "visitors"}
    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=alice.public_key,
        asset=assetdata_tx,
        metadata=asset_metadata
    )

    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=alice.private_key
    )

    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)

    txid = fulfilled_creation_tx['id']

    asset_id = txid

    transfer_asset = {
        'id': asset_id
    }

    output_index = 0
    output = fulfilled_creation_tx['outputs'][output_index]
    return output
