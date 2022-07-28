let tempNum = 1;
let temp = ['./img/screenshot', "2", '.png'];
let cardText = document.getElementById("card-desc");
function prev() {
    if(tempNum > 1) {
        tempNum -= 1;
    }
    temp[1] = tempNum.toString();
    document.getElementById("card-img").src = temp.join("");
    console.log('<')
    setText(tempNum);
}

function next() {
    if (tempNum < 5) {
        tempNum += 1;
    }
    temp[1] = tempNum.toString();
    document.getElementById("card-img").src = temp.join("");
    console.log('>')
    setText(tempNum);
}
function setText(arr) {
    switch(arr) {
        case 1:
            cardText.innerHTML = "1"
            break;
        case 2:
            cardText.innerHTML = "2"
            break;
        case 3:
            cardText.innerHTML = "3"
            break;
        case 4:
            cardText.innerHTML = "4"
            break;
        case 5:
            cardText.innerHTML = "5"
            break;
    }
}
//display:none