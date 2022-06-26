import argparse
import json

ACCOUNT = "account"
BALANCE = "balance"
DECIMAL_COUNT = 9
DECIMAL_MULTIPLIER = 10 ** DECIMAL_COUNT
EXCLUDED_WALLETS = [
    "0x000000000000000000000000000000000000dead".upper()
]
TOTAL_AIRDROP = 100000000000000

def main(wallet_address, include_excluded_wallets):
    with open("wallets.json") as file:
        content = json.loads(file.read())

    running_total = 0
    wallet_total = None

    for entry in content:
        if entry[ACCOUNT].upper() == wallet_address.upper():
            wallet_total = float(entry[BALANCE]) / DECIMAL_MULTIPLIER
        if not include_excluded_wallets and entry[ACCOUNT].upper() in EXCLUDED_WALLETS:
            pass
        else:    
            running_total += float(entry[BALANCE]) / DECIMAL_MULTIPLIER

    if wallet_total == None:
        print("The address provided is not in the airdrop list")
    else:
        percentage_of_total = wallet_total / running_total
        total_airdrop_for_wallet = percentage_of_total * TOTAL_AIRDROP
        percent_increase = total_airdrop_for_wallet / wallet_total
        print("Total Airdrop Amount: " + "{:,}".format(round(total_airdrop_for_wallet, 2)) + " Y5")
        print("Percent Increase in Holdings: " + str(round(percent_increase * 100, 2)) + "%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Y5 Airdrop Calculator')

    parser.add_argument('--address', help='Your Public Binance Smart Chain Address')
    parser.add_argument('--include_excluded_wallets', action='store_true', help='Includes the excluded wallets in the calculation')

    args=parser.parse_args()

    if not str(args.address):
        print("Please enter an address in the --address field and retry")

    main(str(args.address), bool(args.include_excluded_wallets))
    