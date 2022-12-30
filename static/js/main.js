function test (index) {
    var data = {index: index};
    fetch("/run/button/", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }).then(ret => {ret.text().then(output => {
        console.log(output);
    }); });

}

window.addEventListener("load",function() {
    // Refresh the Images:
    fetch("/getjson/", {
        method: "POST",
    }).then(ret => {ret.json().then(jsonData => {
        console.log(jsonData);
        for(var i = 0; i < 12; i++){
            img = document.getElementById(i);
            console.log(jsonData['grid'][i]['image'])
            img.src=jsonData['grid'][i]['image'];
        }
    }); });

    // Refresh the p tag in the middle:
    fetch("/getjson/", {
        method: "POST",
    }).then(ret => {ret.json().then(jsonData => {
        console.log(jsonData);
        for(var i = 0; i < 12; i++){
            txt = document.getElementById('t' + i);
            console.log(jsonData['grid'][i]['text'])
            txt.textContent=jsonData['grid'][i]['text'];
        }
    }); });

  });
