from enchash.algos import *
algoList = ["AES", "ARCFOUR", "BLOWFISH", "CAMELLIA", "CAST", "DES", "IDEA", "TRIPLEDES"]
algoDict = {
    "AES": algo_AES,
    "ARCFOUR": algo_ARCFOUR,
    "BLOWFISH": algo_BLOWFISH,
    "CAMELLIA": algo_CAMELLIA,
    "CAST": algo_CAST,
    "DES": algo_DES,
    "IDEA": algo_IDEA,
    "TRIPLEDES": algo_TRIPLEDES
}

def encryption(key, plaintext, *algo):
    message = plaintext
    applyAlgoList = [algoList[i] for i in range(0, 8) if algo[i]==True]
    for i in applyAlgoList:
        message = algoDict[i](message, "encrypt", key)
    return message

def decryption(key, ciphertext, *algo):
    message = ciphertext
    applyAlgoList = [algoList[i] for i in range(0, 8) if algo[i]==True]
    for i in applyAlgoList[::-1]:
        message = algoDict[i](message, "decrypt", key)
    return message


x = "PleaseHideME,I am plain text"

# a = encryption("Longkeys", x, True, False, False, False, False, True, False, True)
# print(a)

# b = decryption("Longkeys", a, True, False, False, False, False, True, False, True)
# print(b)
