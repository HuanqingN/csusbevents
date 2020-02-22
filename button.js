function on_submit(){
    if(document.getElementById("student").checked){
        location.href = "events.html";
    } else {
            var userid, pwd;
            userid = document.getElementById("userid");
            pwd = document.getElementById("pwd");
    }

    // var url = "localhost:";
    // var xhr = new XMLHttpRequest();
    // xhr.open("GET", url, false);
    // xhr.onload = // something
    // document.getElementById("your_button's_ID").addEventListener("click",
    // function() {xhr.send(data)},
    // false;
    // document.getElementById("submitted").innerHTML="submitted";
}


// function onload(){
//     document.getElementById("submit").onclick = onsubmit();
// }