let encryptBtn = document.getElementById("selfEncryption");
let decryptBtn = document.getElementById("selfDecryption");

encryptBtn.addEventListener("click", function () {
    
    var inputImage = document.getElementById("inputfile").files[0].name; 
    console.log(inputImage)
    var inputImageKey = document.getElementById("inputfile").value;
    // console.log(inputImage);
    fetch("http://127.0.0.1:8000/imageenc", {
        method: "POST",
        body: JSON.stringify({
            "inputImage": inputImage,
            "inputImageKey": inputImageKey,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.text();
    }).then(function (data) {
        document.getElementById("encimage").src = data;
        document.getElementById("hashedImagediv").style.display="block";
        console.log("data = >"+data);   
    });


});


decryptBtn.addEventListener("click", function () {
    var encryptedString = document.getElementById("encryptedString").value;
    var inputkey = document.getElementById("key").value;
    var decalgo1 = document.getElementById("decalgo1").checked;
    var decalgo2 = document.getElementById("decalgo2").checked;
    var decalgo3 = document.getElementById("decalgo3").checked;
    var decalgo4 = document.getElementById("decalgo4").checked;
    var decalgo5 = document.getElementById("decalgo5").checked;
    var decalgo6 = document.getElementById("decalgo6").checked;
    var decalgo7 = document.getElementById("decalgo7").checked;
    var decalgo8 = document.getElementById("decalgo8").checked;
 
    fetch("http://127.0.0.1:8000/clubbingalgosdec", {
        method: "POST",
        body: JSON.stringify({
            "encryptedString": encryptedString,
            "inputkey": inputkey,
            "algo1": decalgo1,
            "algo2": decalgo2,
            "algo3": decalgo3,
            "algo4": decalgo4,
            "algo5": decalgo5,
            "algo6": decalgo6,
            "algo7": decalgo7,
            "algo8": decalgo8,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.text();
    }).then(function (data) {
        document.getElementById("originalwaladiv").style.display="block";
    if(data) {
        if(inputkey == keyString.value) {
            document.getElementById("decryptedStringValue").value=inputString.value;
        }
        else {
            document.getElementById("decryptedStringValue").value="Incorrect Key Value";
        }
        
    }
    else {
        document.getElementById("decryptedStringValue").value="Result Not Found";
    }
        
        console.log(data)
    });
})
