let encryptBtn = document.getElementById("selfEncryption");
let decryptBtn = document.getElementById("selfDecryption");


function makerandomString(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * 
 charactersLength));
   }
   return result;
}


encryptBtn.addEventListener("click", function () {
    console.log("SEND");
    var inputString = document.getElementById("inputString").value;
    var encryptionNormal = document.getElementById("encryptionNormal").checked;
    var changeVowels = document.getElementById("changeVowels").checked;
    var numberOperation = document.getElementById("numberOperation").checked;
    var numberOperationvalue = document.getElementById("numberOperationvalue").value;
    var letterValue = document.getElementById("letterValue").value;

    var randomString = makerandomString(inputString.length);
    localStorage.setItem(randomString, inputString);
 
    fetch("http://127.0.0.1:8000/selfalgo", {
        method: "POST",
        body: JSON.stringify({
            "inputString": randomString,
            "encryptionNormal": encryptionNormal,
            "changeVowels": changeVowels,
            "numberOperation": numberOperation,
            "numberOperationvalue": numberOperationvalue,
            "letterValue": letterValue,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.text();
    }).then(function (data) {
        mydata = data.split(",")
        document.getElementById("keyStringdiv").style.display="block";
        document.getElementById("hashedStringdiv").style.display="block";

        document.getElementById("keyString").value=mydata[0];
        document.getElementById("hashedString").value=mydata[1];
     
    });
});


decryptBtn.addEventListener("click", function () {

    var encryptedString = document.getElementById("encryptedString").value;
    var inputkey = document.getElementById("inputkey").value;
 
    fetch("http://127.0.0.1:8000/selfalgodec", {
        method: "POST",
        body: JSON.stringify({
            "encryptedString": encryptedString,
            "inputkey": inputkey,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.text();
    }).then(function (data) {

    var ReversedString = localStorage.getItem(data);
    localStorage.removeItem(data);
    if(ReversedString) {
        document.getElementById("decryptedStringValue").value=ReversedString;
    }
    else {
        document.getElementById("decryptedStringValue").value="Result Not Found";
    }
        
        console.log(data)
    });
})
