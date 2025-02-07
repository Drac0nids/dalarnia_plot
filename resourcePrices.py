import time

from web3 import Web3
import json
bsc_mainnet_url = "https://bsc-dataseed.binance.org/"
bsc_mainnet_url2 = "https://nd-925-819-351.p2pify.com/5b2788aca1e7e4db27ff83f28fe2809d"
web3 = Web3(Web3.HTTPProvider(bsc_mainnet_url2))

copperSwap_contract_address = "0x92fE453dD29Ceb6C631CB06CCeC50f23e1220d14"
ironSwap_contract_address = "0xCA9160F5637D7160168Ee2064741e17cC31A0D29"
silverSwap_contract_address = "0x2337560a89FC03932b46fCcdd688E4E1D8225f26"
ozySwap_contract_address = "0xc1f88f29bef04DFa24d60B60252125BF76EC7E79"
goldSwap_contract_address = "0x81D137990ab95F6f13218cffC796587BC1986e77"
ragnariteSwap_contract_address = "0x214DA57D6E51E4f7BB3e93c6d0bfFA02f2ae6C64"
aquariteSwap_contract_address = "0x2129Ab129C661D0209FfcF29E4d32B74BcC3090c"
craftSwap_contract_address = "0x96dfBD2C945Bca02378FfD8e4593054d098E8bAc"
combineSwap_contract_address = "0xE49e8f1a7bf5Dd83986BE1d527A7b4084AcC3a3b"
stellarSwap_contract_address = "0x5922800a0e93b7163F190C4a1528adA8Af925a49"

swap_contract_abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"swapper","type":"address"},{"indexed":false,"internalType":"uint256","name":"resourceId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dar","type":"uint256"}],"name":"SwapResourceIn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"swapper","type":"address"},{"indexed":false,"internalType":"uint256","name":"resourceId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dar","type":"uint256"}],"name":"SwapResourceOut","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FACTORY","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LIQUIDITY_PROVIDER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_darAmount","type":"uint256"},{"internalType":"uint256","name":"_resourceAmount","type":"uint256"}],"name":"addLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"dar","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_resourceIn","type":"uint256"},{"internalType":"uint256","name":"_resourceOut","type":"uint256"}],"name":"getCurrentSwapValue","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPairBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_dar","type":"address"},{"internalType":"address","name":"_resources","type":"address"},{"internalType":"uint256","name":"_resourceId","type":"uint256"},{"internalType":"address","name":"_singleApproveTransfer","type":"address"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_resourceTracker","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"kMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"pausePair","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_percent","type":"uint256"}],"name":"removeLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"resourceId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"resourceTracker","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"resources","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"singleApproveTransfer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_resourceIn","type":"uint256"},{"internalType":"uint256","name":"_resourceOut","type":"uint256"},{"internalType":"uint256","name":"_darAmount","type":"uint256"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpausePair","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_resourceTracker","type":"address"}],"name":"updateResourceTracker","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""

copperSwap_contract = web3.eth.contract(address=copperSwap_contract_address, abi=swap_contract_abi)
ironSwap_contract = web3.eth.contract(address=ironSwap_contract_address, abi=swap_contract_abi)
silverSwap_contract = web3.eth.contract(address=silverSwap_contract_address, abi=swap_contract_abi)
ozySwap_contract = web3.eth.contract(address=ozySwap_contract_address, abi=swap_contract_abi)
goldSwap_contract = web3.eth.contract(address=goldSwap_contract_address, abi=swap_contract_abi)
ragnariteSwap_contract = web3.eth.contract(address=ragnariteSwap_contract_address, abi=swap_contract_abi)
aquariteSwap_contract = web3.eth.contract(address=aquariteSwap_contract_address, abi=swap_contract_abi)
craftSwap_contract = web3.eth.contract(address=craftSwap_contract_address, abi=swap_contract_abi)
combineSwap_contract = web3.eth.contract(address=combineSwap_contract_address, abi=swap_contract_abi)
stellarSwap_contract = web3.eth.contract(address=stellarSwap_contract_address, abi=swap_contract_abi)


def pkToAddress(pk):
    account = web3.eth.account.from_key(pk)
    return account.address

def getCurrentSwapValue(resource,_resourceIn,_resourceOut):
    if resource == "copper":
        try:
            swap_value = copperSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "iron":
        try:
            swap_value = ironSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "silver":
        try:
            swap_value = silverSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "ozy":
        try:
            swap_value = ozySwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "gold":
        try:
            swap_value = goldSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "ragnarite":
        try:
            swap_value = ragnariteSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "aquarite":
        try:
            swap_value = aquariteSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "craft":
        try:
            swap_value = craftSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "combine":
        try:
            swap_value = combineSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)
    elif resource == "stellar":
        try:
            swap_value = stellarSwap_contract.functions.getCurrentSwapValue(_resourceIn, _resourceOut).call()
            return swap_value
        except Exception as e:
            print(e)

def getPrice():
    copper = getCurrentSwapValue("copper",1,0)/1000000
    iron = getCurrentSwapValue("iron",1,0)/1000000
    silver = getCurrentSwapValue("silver",1,0)/1000000
    ozy = getCurrentSwapValue("ozy", 1, 0) / 1000000
    gold = getCurrentSwapValue("gold", 1, 0) / 1000000
    ragnarite = getCurrentSwapValue("ragnarite", 1, 0) / 1000000
    aquarite = getCurrentSwapValue("aquarite", 1, 0) / 1000000
    craft = getCurrentSwapValue("craft", 1, 0) / 1000000
    combine = getCurrentSwapValue("combine", 1, 0) / 1000000
    stellar = getCurrentSwapValue("stellar", 1, 0) / 1000000
    return copper,iron,silver,ozy,gold,ragnarite,aquarite,craft,combine,stellar

def save_prices_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
def swap(pk,resource,_resourceIn,_resourceOut,_darAmount):
    address = pkToAddress(pk)
    params = {
        "from": address,
        "value": 0,
        'gasPrice': web3.to_wei(1, 'gwei'),
        "gas": 132468,
        "nonce": web3.eth.get_transaction_count(address),
    }
    if resource == "copper":
        func = copperSwap_contract.functions.swap(_resourceIn,_resourceOut,_darAmount)
    elif resource == "iron":
        func = ironSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "ozy":
        func = ozySwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "gold":
        func = goldSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "ragnarite":
        func = ragnariteSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "aquarite":
        func = aquariteSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "craft":
        func = craftSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)
    elif resource == "combine":
        func = combineSwap_contract.functions.swap(_resourceIn, _resourceOut, _darAmount)

    tx = func.build_transaction(params)
    try:
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=pk)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print("https://bscscan.com/tx/"+"0x"+tx_hash.hex())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        copper, iron, silver, ozy, gold, ragnarite, aquarite, craft, combine, stellar = getPrice()
        prices_data = {
            'copper': copper,
            'iron': iron,
            'silver': silver,
            'ozy': ozy,
            'gold': gold,
            'ragnarite': ragnarite,
            'aquarite': aquarite,
            'craft': craft,
            'combine': combine,
            'stellar': stellar
        }
        print(prices_data)
        save_prices_to_json(prices_data, 'prices.json')
        time.sleep(10)