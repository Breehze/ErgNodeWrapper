# ErgNodeWrapper
## Initializing node

Node(api key,wallet password,node address,node ip)

## Node methods

**.send_payment_tx(address,erg_value,assets)** - sends tx with ERG/assets , retruns tx id

**.unlock_wallet()** - unlocks wallet

**.get_tokens()** - returns dict with tokenId-amount pair

**.get_erg_balance()** - returns erg balance of the node wallet

**.get_transactons()** - returns list of wallet related transactions

**.get_boxId_byIdBinary(boxId)** -  returns binary id ~~(I guess)~~

**.get_transaction_byId(txId)** - returns tx by transaction id

**.get_address_ergotree** - returns ergo tree of node address