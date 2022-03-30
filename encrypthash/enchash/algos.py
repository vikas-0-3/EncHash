# IMPORTS
import base64
try:
    from cryptography.hazmat.primitives import hashes, padding
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from Crypto.Cipher import Blowfish, DES
    from Crypto.Util.Padding import pad, unpad
except ModuleNotFoundError as e:
    print("Cryptography or Crypto module is missing :'( ")
    print("pip install cryptography")
    print("pip install pycrypto")

# Functions
# AES
def algo_AES(string, do, key):
    # Key generation
    def makeKEY():
        salt = b'some salt'
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(key.encode()))
    # Get fernet object
    def getFernetObj():
        return Fernet(makeKEY())
    # main function
    if do == "encrypt":
        return getFernetObj().encrypt(string.encode()).decode()
    elif do == "decrypt":
        return getFernetObj().decrypt(string.encode()).decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# Arcfour
def algo_ARCFOUR(string, do, key):
    # Key length fix
    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [40, 56, 64, 80, 128, 192, 256]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    algorithm = algorithms.ARC4(key.encode())
    cipher = Cipher(algorithm, mode=None)

    # main function
    if do == "encrypt":
        encryptor = cipher.encryptor()
        ct = encryptor.update(string.encode())
        return ct.decode("latin-1")
    elif do == "decrypt":
        decryptor = cipher.decryptor()
        pt = decryptor.update(string.encode("latin-1"))
        return pt.decode("latin-1")
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# Blowfish
def algo_BLOWFISH(string, do, key):
    # MAIN FUNCTION
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    bs = Blowfish.block_size
    # Call handling
    if do == "encrypt":
        return cipher.encrypt(pad(string.encode(), bs)).decode("latin-1")
    elif do == "decrypt":
        msg = cipher.decrypt(string.encode("latin-1"))
        return unpad(msg, bs).decode("latin-1")
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# Camellia
def algo_CAMELLIA(string, do, key):
    def go_encrypt(msg,method,mode):
        cipher = Cipher(method, mode)
        encryptor = cipher.encryptor()
        ct = encryptor.update(msg) + encryptor.finalize()
        return (ct)
    def go_decrypt(ct,method,mode):
        cipher = Cipher(method, mode)
        decryptor = cipher.decryptor()
        return (decryptor.update(ct) + decryptor.finalize())
    def pad(data,size=128):
        padder = padding.PKCS7(size).padder()
        padded_data = padder.update(data)
        padded_data += padder.finalize()
        return(padded_data)
    def unpad(data,size=128):
        padder = padding.PKCS7(size).unpadder()
        unpadded_data = padder.update(data)
        unpadded_data += padder.finalize()
        return(unpadded_data)

    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [128, 192, 256]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    # main function
    if do == "encrypt":
        padded_data=pad(string.encode())
        cipher=go_encrypt(padded_data,algorithms.Camellia(key.encode()), modes.ECB())
        return cipher.decode("latin-1")
    elif do == "decrypt":
        plain=go_decrypt(string.encode("latin-1"),algorithms.Camellia(key.encode()), modes.ECB())
        data=unpad(plain)
        return data.decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# Cast
def algo_CAST(string, do, key):
    def go_encrypt(msg,method,mode):
        cipher = Cipher(method, mode)
        encryptor = cipher.encryptor()
        ct = encryptor.update(msg) + encryptor.finalize()
        return (ct)

    def go_decrypt(ct,method,mode):
        cipher = Cipher(method, mode)
        decryptor = cipher.decryptor()
        return (decryptor.update(ct) + decryptor.finalize())

    def pad(data,size=128):
        padder = padding.PKCS7(size).padder()
        padded_data = padder.update(data)
        padded_data += padder.finalize()
        return(padded_data)

    def unpad(data,size=128):
        padder = padding.PKCS7(size).unpadder()
        unpadded_data = padder.update(data)
        unpadded_data += padder.finalize()
        return(unpadded_data)

    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [40,128]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    # main function
    if do == "encrypt":
        padded_data=pad(string.encode())
        cipher=go_encrypt(padded_data,algorithms.CAST5(key.encode()), modes.ECB())
        return cipher.decode("latin-1")
    elif do == "decrypt":
        plain=go_decrypt(string.encode("latin-1"),algorithms.CAST5(key.encode()), modes.ECB())
        data=unpad(plain)
        return data.decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# DES
def algo_DES(string, do, key):
    # Takes first 8 characters only, rest are ignored
    # Hence result is same when key is: "key12345" or "key123456"
    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [64]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    des = DES.new(key[:8].encode(), DES.MODE_ECB)
    # main function
    if do == "encrypt":
        padded_text = pad(string.encode(), 64)
        encrypted_text = des.encrypt(padded_text)
        return encrypted_text.decode("latin-1")
    elif do == "decrypt":
        return unpad(des.decrypt(string.encode("latin-1")), 64).decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# IDEA
def algo_IDEA(string, do, key):
    def go_encrypt(msg,method,mode):
        cipher = Cipher(method, mode)
        encryptor = cipher.encryptor()
        ct = encryptor.update(msg) + encryptor.finalize()
        return (ct)
    def go_decrypt(ct,method,mode):
        cipher = Cipher(method, mode)
        decryptor = cipher.decryptor()
        return (decryptor.update(ct) + decryptor.finalize())
    def pad(data,size=128):
        padder = padding.PKCS7(size).padder()
        padded_data = padder.update(data)
        padded_data += padder.finalize()
        return(padded_data)
    def unpad(data,size=128):
        padder = padding.PKCS7(size).unpadder()
        unpadded_data = padder.update(data)
        unpadded_data += padder.finalize()
        return(unpadded_data)

    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [128]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    # main function
    if do == "encrypt":
        padded_data=pad(string.encode())
        cipher=go_encrypt(padded_data,algorithms.IDEA(key[:16].encode()), modes.ECB())
        return cipher.decode("latin-1")
    elif do == "decrypt":
        plain=go_decrypt(string.encode("latin-1"),algorithms.IDEA(key[:16].encode()), modes.ECB())
        data=unpad(plain)
        return data.decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")
# TripleDES
def algo_TRIPLEDES(string, do, key):
    def go_encrypt(msg,method,mode):
        cipher = Cipher(method, mode)
        encryptor = cipher.encryptor()
        ct = encryptor.update(msg) + encryptor.finalize()
        return (ct)
    def go_decrypt(ct,method,mode):
        cipher = Cipher(method, mode)
        decryptor = cipher.decryptor()
        return (decryptor.update(ct) + decryptor.finalize())
    def pad(data,size=128):
        padder = padding.PKCS7(size).padder()
        padded_data = padder.update(data)
        padded_data += padder.finalize()
        return(padded_data)
    def unpad(data,size=128):
        padder = padding.PKCS7(size).unpadder()
        unpadded_data = padder.update(data)
        unpadded_data += padder.finalize()
        return(unpadded_data)

    chars="4g6t13kfvbldhi0csnrepm87wo5z2yxqaju9"
    bitLength = [128]
    keyLen_inBits = len(key)
    if keyLen_inBits not in bitLength:
        addMore = [keyLen_inBits - (i//8) for i in bitLength]
        for i in addMore:
            if i < 0:
                key = key + chars[0:i*-1]
                break
    # main function
    if do == "encrypt":
        padded_data=pad(string.encode())
        cipher=go_encrypt(padded_data,algorithms.TripleDES(key[:16].encode()), modes.ECB())
        return cipher.decode("latin-1")
    elif do == "decrypt":
        plain=go_decrypt(string.encode("latin-1"),algorithms.TripleDES(key[:16].encode()), modes.ECB())
        data=unpad(plain)
        return data.decode()
    else:
        raise Exception(f"INVALID OPERATION: '{do}'")

# Main
if __name__ == "__main__":
    print("This module contains cryptographic algorithms for encryption and decryption. This module cannot be run as a separate entity.")