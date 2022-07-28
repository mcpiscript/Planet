let tempNum = 1;
let temp = ['./img/screenshot', "2", '.png'];
let cardText = document.getElementById("card-desc");
function prev() {
    if(tempNum > 1) {
        tempNum -= 1;
    }
    temp[1] = tempNum.toString();
    document.getElementById("card-img").src = temp.join("");
    setText(tempNum);
}

function next() {
    if (tempNum < 5) {
        tempNum += 1;
    }
    temp[1] = tempNum.toString();
    document.getElementById("card-img").src = temp.join("");
    setText(tempNum);
}
function setText(arr) {
    switch(arr) {
        case 1:
            cardText.innerText = "Planet launcher";
            break;
        case 2:
            cardText.innerText = "2";
            break;
        case 3:
            cardText.innerText = "3";
            break;
        case 4:
            cardText.innerText = "4";
            break;
        case 5:
            cardText.innerText = "5";
            break;
        default: 
            cardText.innerText = "Planet launcher";
            break;
    }
    console.log(arr)
}


window.onload = function () {
};