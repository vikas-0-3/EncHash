def algo_AES(string, do, key):
    # IMPORTS
    import base64
    try:
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        from cryptography.fernet import Fernet
    except ModuleNotFoundError as e:
        print("Cryptography module is missing :'( ")
        print("pip install cryptography")

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

# x = algo_AES("hello", "encrypt", "thisKEY")
# y = algo_AES(x, "decrypt", "thisKEY")
# print("x: ",x)
# print("y: ",y)