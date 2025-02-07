from web3 import Web3
import sqlite3
import time
import random
bsc_mainnet_url2 = "https://nd-925-819-351.p2pify.com/5b2788aca1e7e4db27ff83f28fe2809d"
web3 = Web3(Web3.HTTPProvider(bsc_mainnet_url2))

plotState_contract_address = "0x456803Fc1fC3c4Ad245046E3395d78ddeE7F70B8"

plotstate_contract_abi = """[{"inputs":[{"internalType":"contract IPlanetPlot","name":"_planetPlot","type":"address"},{"internalType":"address","name":"default_admin","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PLANET_PLOT_HANDLER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PLOT_CREATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"PlotState","outputs":[{"internalType":"uint256","name":"max","type":"uint256"},{"internalType":"uint256","name":"left","type":"uint256"},{"internalType":"uint256","name":"rent","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_renter","type":"address"},{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_addDigs","type":"uint256"}],"name":"addAddressIsRenting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressIsRenting","outputs":[{"internalType":"uint256","name":"digs","type":"uint256"},{"internalType":"uint256","name":"plot","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_plotIds","type":"uint256[]"}],"name":"createPlot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"}],"name":"getLeft","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"}],"name":"getMax","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"}],"name":"getRent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_player","type":"address[]"},{"internalType":"uint256[]","name":"_plots","type":"uint256[]"},{"internalType":"uint256[]","name":"_digsOpen","type":"uint256[]"}],"name":"portOverDigs","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_renter","type":"address"},{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_digs","type":"uint256"}],"name":"setAddressIsRenting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_newLeft","type":"uint256"}],"name":"setLeft","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_newMax","type":"uint256"}],"name":"setMax","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_max","type":"uint256"},{"internalType":"uint256","name":"_left","type":"uint256"},{"internalType":"uint256","name":"_rent","type":"uint256"}],"name":"setPlot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_newRent","type":"uint256"}],"name":"setRent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_renter","type":"address"},{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_subDigs","type":"uint256"}],"name":"subAddressIsRenting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_plotId","type":"uint256"},{"internalType":"uint256","name":"_sub","type":"uint256"}],"name":"subLeft","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]"""

plotState_contract = web3.eth.contract(address=plotState_contract_address, abi=plotstate_contract_abi)

def getPlotState(plotId):
    try:
        plotState = plotState_contract.functions.PlotState(plotId).call()
        return plotState
    except Exception as e:
        print(e)
def checkState():
    conn = sqlite3.connect('plotstate.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT plotId,rent,left FROM plot")
        for db_plotState in cursor.fetchall():
            plotId = db_plotState[0]
            db_rent = db_plotState[1]
            db_left = db_plotState[2]
            #print(plotId,db_rent,db_left)
            contract_plotState = getPlotState(plotId)
            time.sleep(1)
            contract_rent = contract_plotState[2]/1000000
            contract_left = contract_plotState[1]
            #print(contract_rent,contract_left)
            #print(db_rent!=contract_rent)
            if db_rent!=contract_rent:
                try:
                    # 执行 SQL 更新语句
                    cursor.execute("""
                            UPDATE plot
                            SET rent = ?
                            WHERE plotId = ?
                        """, (contract_rent, plotId))
                    conn.commit()
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
            #print(db_left!=contract_left)
            if db_left!=contract_left:
                try:
                    # 执行 SQL 更新语句
                    cursor.execute("""
                            UPDATE plot
                            SET left = ?
                            WHERE plotId = ?
                        """, (contract_left, plotId))
                    conn.commit()
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    while True:
        checkState()
