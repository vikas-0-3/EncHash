import base64

mystr = "vikas 123 VIKAS #03"

def vowelsConvert(str):
  string = list(str)
  for i in range(len(string)):
    
    if string[i] == "a":
        string[i] = "@"
    if string[i] == "A":
        string[i] = "^"

    if string[i] == "e":
        string[i] = "$"
    if string[i] == "E":
        string[i] = "&"

    if string[i] == "i":
        string[i] = "!"
    if string[i] == "I":
        string[i] = "|"

    if string[i] == "o":
        string[i] = "("
    if string[i] == "O":
        string[i] = ")"

    if string[i] == "u":
        string[i] = "["
    if string[i] == "U":
        string[i] = "]"
      
      
  return string


def vowelsDecrypt(str):

  string = list(str)
  for i in range(len(string)):
    
    if string[i] == "@":
        string[i] = "a"
    if string[i] == "^":
        string[i] = "A"

    if string[i] == "$":
        string[i] = "e"
    if string[i] == "&":
        string[i] = "E"

    if string[i] == "!":
        string[i] = "i"
    if string[i] == "|":
        string[i] = "I"

    if string[i] == "(":
        string[i] = "o"
    if string[i] == ")":
        string[i] = "O"

    if string[i] == "[":
        string[i] = "u"
    if string[i] == "]":
        string[i] = "U"
      
      
  return string



def ConvertToAscii(mystr):
    str2 = [ord(c) for c in mystr]
    return str2

def DecodeAscii(mystr):
    data = ''.join(chr(i) for i in mystr)
    return data

def IncrementMe(mystr, n):
    value = ''.join(map(lambda x:chr(ord(x)+n),mystr))
    return value

def DecrementMe(mystr, n):
    value = ''.join(map(lambda x:chr(ord(x)-n),mystr))
    return value

def MultiplyMe(mystr, n):
    value = ''.join(map(lambda x:chr(ord(x)*n),mystr))
    return value

def DivideMe(mystr, n):
    value = ''.join(map(lambda x:chr(ord(x)//n),mystr))
    return value

def ConvertToBase64(mystr):
    data = base64.b64encode(mystr)
    return data

def DecodeBase64(mystr):
    data = base64.b64decode(mystr).decode('utf-8')
    return data



# print("ascii => " + str(ConvertToAscii(mystr)))
# print("Increment => " + str(IncrementMe(mystr, 5)))
# print("Decrement => " + str(DecrementMe(mystr, 5)))
# print("Normal => " + str(IncrementMe(DecrementMe(mystr, 5), 5)))
# print("Decode B64=> " + str(DecodeAscii(ConvertToAscii(mystr))) )
# print("Increment => " + str(IncrementMe(mystr, 5)))
# print("Decrement => " + str(DecrementMe(mystr, 5)))
# print("Multiply => " + str(MultiplyMe(mystr, 5)))
# print("Divide => " + str(DivideMe(mystr, 5)))
# print("*******************************************")
# print("Multiply => " + str(DivideMe(MultiplyMe(mystr, 5),5)))
# print("Divide => " + str(MultiplyMe(DivideMe(mystr, 5),5)))



# print(vowelsConvert(mystr))
# print(vowelsDecrypt(vowelsConvert(mystr)))
# print(IncrementMe(mystr, 1))
