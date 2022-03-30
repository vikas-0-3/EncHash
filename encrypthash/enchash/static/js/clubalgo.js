let encryptBtn = document.getElementById("selfEncryption");
let decryptBtn = document.getElementById("selfDecryption");

encryptBtn.addEventListener("click", function () {
    console.log("CLUBBING aLgos");
    var inputString = document.getElementById("inputString").value;
    var keyString = document.getElementById("keyString").value;
    var algo1 = document.getElementById("algo1").checked;
    var algo2 = document.getElementById("algo2").checked;
    var algo3 = document.getElementById("algo3").checked;
    var algo4 = document.getElementById("algo4").checked;
    var algo5 = document.getElementById("algo5").checked;
    var algo6 = document.getElementById("algo6").checked;
    var algo7 = document.getElementById("algo7").checked;
    var algo8 = document.getElementById("algo8").checked;
    
 
    fetch("http://127.0.0.1:8000/clubbingalgos", {
        method: "POST",
        body: JSON.stringify({
            "inputString": inputString,
            "inputKey": keyString,
            "algo1": algo1,
            "algo2": algo2,
            "algo3": algo3,
            "algo4": algo4,
            "algo5": algo5,
            "algo6": algo6,
            "algo7": algo7,
            "algo8": algo8,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.text();
    }).then(function (data) {
        document.getElementById("hashedStringdiv").style.display="block";
        document.getElementById("hashedString").value=data;     
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
        document.getElementById("decryptedStringValue").value=data;
    }
    else {
        document.getElementById("decryptedStringValue").value="Result Not Found";
    }
        
        console.log(data)
    });
})
