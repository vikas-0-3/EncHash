from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

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


# a = algo_ARCFOUR("ThundeR", "encrypt", "SomeKey")
# b = algo_ARCFOUR(a, "decrypt", "SomeKey")
# print("a: ",a)
# print("b: ",b)
