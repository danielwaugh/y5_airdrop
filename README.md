# Y5 Airdrop Calculator

The Y5 Airdrop Calculator handles calculating the amount you will receive from the airdrop.

The Script Determines if the entered wallet is present in the airdrop list and calculates the total airdrop amount if everything is equally distributed.

The Dead Wallet is excluded from the calculation unless specified by argument

## Usage

```bash
python3 main.py --help

python3 main.py --address <bsc_public_address>

python3 main.py --address <bsc_public_address> --include_excluded_wallets
```