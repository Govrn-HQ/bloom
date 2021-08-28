## Purpose
Create a command line interface of a publicly downloadable desktop wallet with the following features. (Note: I still need to dockerize the project.)

## Features
1. Generates asymmetric keys 
2. Signs a text message
3. Verifies signatures
4. Encrypts a text message
5. Decrypts a text message

## Design Considerations
This is a stand alone implementation, for simplicity.  Wallet does not interact with other wallets but relies on user inputs through the command line. Uses ECDSA algorithm for signing and ECIES for encryption/decryption. Keys are asymmetric.

## Dependencies
Python: eth_keys, eth_utils, binascii, ecies

## Helpful resources
[Practical cryptography for developers](https://cryptobook.nakov.com/asymmetric-key-ciphers/ecies-example)

[eth-keys repo](https://github.com/ethereum/eth-keys)
