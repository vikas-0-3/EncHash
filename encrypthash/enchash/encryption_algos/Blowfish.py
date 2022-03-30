def algo_BLOWFISH(string, do, key):
    # IMPORTS
    from Crypto.Cipher import Blowfish
    from Crypto.Util.Padding import pad, unpad
    
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


# x = algo_BLOWFISH("ThundeR", "encrypt", "thisKey")
# y = algo_BLOWFISH(x, "decrypt", "thisKey")
# print("x: ",x)
# print("y: ",y)
