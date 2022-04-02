from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from enchash.selfalgo import *
from enchash.clubbing import *
import json
from enchash.static.imagecrypto.rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image
from django.conf.urls.static import static
# base 1

def home(request):
    return render(request, "base.html", {})

def textencryption(request):
    return render(request, "base.html", {})

def imageencryption(request):
    return render(request, "base.html", {})

def clubalgo(request):
    return render(request, "base.html", {})

# base 2
def urlMe(request):
    return render(request, "base.html", {})


@csrf_exempt
def imageenc(request):
    if request.method == 'POST':

        body_data = request.body.decode("utf-8")
        bodydata = json.loads(body_data)
        inputImg = "C:\\Users\\vg123\\OneDrive\\Pictures\\"+bodydata["inputImage"]
        print(inputImg)

        print("--------------")

        key = bodydata["inputImageKey"]
        output_image = "C:\\Users\\vg123\\OneDrive\\Documents\\GITTU\\EncHash\\encrypthash\\enchash\\static\\imagecrypto\\example\\enc_"+bodydata["inputImage"]
        # output_image = "http://127.0.0.1:8000/static/imagecrypto/example/encryption.png"
        # output_image = static(output_img)
        image = inputImg
        input_image = Image.open(image)
        rubixCrypto = RubikCubeCrypto(input_image)
        print(key)

        print(output_image)

        encrypted_image = rubixCrypto.encrypt(alpha=8, iter_max=10, key_filename=key)
        print("Working here")
        encrypted_image.save(output_image)




        return HttpResponse(output_image)
    return render(request, "base.html", {})



@csrf_exempt
def clubbingalgos(request):
    context = {}
    if request.method == 'POST':
        body_data = request.body.decode("utf-8")
        bodydata = json.loads(body_data)
        inputString = bodydata["inputString"]
        inputString = bodydata["inputString"]
        inputKey = bodydata["inputKey"]
        algo1 = bodydata["algo1"]
        algo2 = bodydata["algo2"]
        algo3 = bodydata["algo3"]
        algo4 = bodydata["algo4"]
        algo5 = bodydata["algo5"]
        algo6 = bodydata["algo6"]
        algo7 = bodydata["algo7"]
        algo8 = bodydata["algo8"]
        a = encryption(inputKey, inputString, algo1, algo2, algo3, algo4, algo5, algo6, algo7, algo8)
        print(a)
        return HttpResponse(a)
    return render(request, "base.html", context)

@csrf_exempt
def clubbingalgosdec(request):
    context = {}
    if request.method == 'POST':
        body_data = request.body.decode("utf-8")
        bodydata = json.loads(body_data)
        inputString = bodydata["encryptedString"]
        inputKey = bodydata["inputkey"]
        algo1 = bodydata["algo1"]
        algo2 = bodydata["algo2"]
        algo3 = bodydata["algo3"]
        algo4 = bodydata["algo4"]
        algo5 = bodydata["algo5"]
        algo6 = bodydata["algo6"]
        algo7 = bodydata["algo7"]
        algo8 = bodydata["algo8"]
        a = "encrypted string dummy"
        try:
            a = decryption(inputKey, inputString, algo1, algo2, algo3, algo4, algo5, algo6, algo7, algo8)
        except Exception as e:
            print("\n")
        return HttpResponse(a)
    return render(request, "base.html", context)

@csrf_exempt
def selfalgo(request):
    context = {}
    if request.method == 'POST':
        body_data = request.body.decode("utf-8")
        bodydata = json.loads(body_data)

        original_string = bodydata["inputString"]
        enc_normal = bodydata["encryptionNormal"]
        cv = bodydata["changeVowels"]
        number_operation = bodydata["numberOperation"]
        numberValue = bodydata["numberOperationvalue"]
        letterValue = bodydata["letterValue"]

        key = "key"
        dec_str = original_string

        if(enc_normal):
            key+="::EN"
            dec_str = ConvertToBase64(bytes(dec_str, 'utf-8')).decode("utf-8")

        if(cv):
            key+="::CV"
            dec_str = vowelsConvert(dec_str)

        if(number_operation):
            key+="::"+str(numberValue)+":"+str(letterValue)
            if(numberValue == "ILV"):
                dec_str = IncrementMe(dec_str, int(letterValue))
            elif(numberValue == "DLV"):
                dec_str = DecrementMe(dec_str, int(letterValue))
            else:
                dec_str = MultiplyMe(dec_str, int(letterValue))
        print(dec_str)

        dec_str2 =  ConvertToAscii(dec_str)
        mykey = ConvertToBase64(bytes(key, 'utf-8')).decode("utf-8")
        decryptedstring = ConvertToBase64(bytes("".join(str(dec_str2)), 'utf-8')).decode("utf-8")
        returnstring = mykey+","+decryptedstring
        return HttpResponse(returnstring)

    return render(request, "base.html", context)

@csrf_exempt
def selfalgo2(request):
    context = {}
    data=""
    if request.method == "POST":
        body_data = request.body.decode("utf-8")
        bodydata = json.loads(body_data)

        encryptedString = bodydata["encryptedString"]
        inputkey = bodydata["inputkey"]
        keylist = DecodeBase64(inputkey).split("::")
        
        if(len(keylist) > 1):
            tempstr=""
            mydecstr = DecodeBase64(encryptedString).strip("[] ").replace(" ", "").split(",")
            for i in mydecstr:
                tempstr+=chr(int(i))

            for i in range(len(keylist)-1, 0, -1):
                if(keylist[i].find(":") > -1):
                    x = keylist[i].split(":")
                    if(x[0] == "ILV"):
                        tempstr = DecrementMe(tempstr, int(x[1]))
                    elif(x[0] == "DLV"):
                        tempstr = IncrementMe(tempstr, int(x[1]))
                    else:
                        tempstr = DivideMe(tempstr, int(x[1]))

                if(keylist[i] == "CV"):
                    tempstr = vowelsDecrypt(tempstr)
                    for ele in tempstr: 
                        data += ele


                if(keylist[i] == "EN"):
                    data = DecodeBase64(data)
            
        else:
            mydecstr = DecodeBase64(encryptedString).strip("[] ").replace(" ", "").split(",")
            for i in mydecstr:
                data+=chr(int(i))
            

        return HttpResponse(data)

    return render(request, "base.html", context)
