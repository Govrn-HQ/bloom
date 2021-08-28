import eth_keys, eth_utils, binascii, os, sys
from ecies import encrypt, decrypt

# generate public and private keys with ECDSA
privKey = eth_keys.keys.PrivateKey(os.urandom(32))
pubKey = privKey.public_key
address = pubKey.to_checksum_address()
print('Private key is: ', privKey, '\n')
print('Public Key is: ', pubKey, '\n')
print('Signer address: ', address, '\n')

# sign messages
msg = input('Enter your secret message: \n')
bmsg = msg.encode()
msgHash = eth_utils.keccak(bmsg)
signature = privKey.sign_msg(bmsg)

print('Msg:', msg, '\n')
print('Msg hash:', binascii.hexlify(msgHash), '\n')
print('Signature: [v = {0}, r = {1}, s = {2}]'.format(
  hex(signature.v), hex(signature.r), hex(signature.s)),'\n')
print('Signature (130 hex digits):', signature, '\n')

# verify signature
print("Now let's pretend you're someone else, who wants to verify that you sent this message.")
isValid = pubKey.verify_msg(bmsg, signature)
print('The message is valid: ', isValid, '\n')

# encrypt a message
print('Now lets encrypt the message you entered earlier. \n')
encrypted = encrypt(privKey.public_key.to_hex(), bmsg)
print("Encrypted:", binascii.hexlify(encrypted), '\n')

# decrypt a message
print('Now lets decrypt the message! \n')
decrypted = decrypt(privKey.to_hex(), encrypted)
print("Decrypted:", decrypted)
