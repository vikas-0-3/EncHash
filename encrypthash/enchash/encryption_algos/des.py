def algo_DES(string, do, key):
    # IMPORTS
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import pad, unpad
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

# x = algo_DES("ThundeR", "encrypt", "thisKey")
# y = algo_DES(x, "decrypt", "thisKey")
# print("x: ",x)
# print("y: ",y)

