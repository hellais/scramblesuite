import time
import pickle
import const
import mycrypto

from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256

def doshit():

    IV_LENGTH = 16
    HMAC_KEY_LENGTH = 32
    AES_KEY_LENGTH = 16

    HMACKey = mycrypto.strong_random(HMAC_KEY_LENGTH)
    AESKey = mycrypto.strong_random(AES_KEY_LENGTH)
    IV = mycrypto.strong_random(IV_LENGTH)
    state = mycrypto.strong_random(112)

    aes = AES.new(AESKey, mode=AES.MODE_CBC, IV=IV)

    encrypted = mycrypto.strong_random(80)

    cryptedState = aes.encrypt(state)

    # Authenticate ticket name, IV and the encrypted state.
    hmac = HMAC.new(HMACKey, IV + \
                    cryptedState, digestmod=SHA256).digest()

    ticket = IV + cryptedState + hmac

    hmac = HMAC.new(HMACKey, ticket, digestmod=SHA256).digest()

    # Decrypt ticket to obtain state.
    aes = AES.new(AESKey, mode=AES.MODE_CBC, IV=ticket[0:16])
    plainTicket = aes.decrypt(ticket)

i = 0
last = time.time()
interval = 1000 * 1000
while True:
    i += 1
    if i % interval:
        speed = interval/(time.time() - last)
        print speed
        last = time.time()
    doshit()

