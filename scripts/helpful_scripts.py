from brownie import accounts,network,config

FORKED_LOCAL_ENVIRONMENT = ['mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENT = ['development', 'ganache-local']

def get_account(index=None,id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
