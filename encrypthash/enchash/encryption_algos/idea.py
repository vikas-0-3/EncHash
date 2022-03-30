def algo_IDEA(string, do, key):
    # IMPORTS
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
    from cryptography.hazmat.primitives import padding
    
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

# x = algo_IDEA("ThundeR", "encrypt", "thekey")
# y = algo_IDEA(x, "decrypt", "thekey")
# print("x: ",x)
# print("y: ",y)
