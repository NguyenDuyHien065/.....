// var header = document.querySelector(".header")
// var container = document.querySelector("#container")

// header.innerText = "This is header"
// container.innerHTML = "<p> this is a P tag :)) </p>"

// header.addEventListener("click", (event) => {
//     // header.style.color = "blue";
//     event.target.innerHTML = "<p> Supprise  :)) </p>"
    
// })
var quizz = document.querySelector("#default-code");
var message = document.querySelector("#message");
var reset = document.querySelector("#reset")
var numColors = 6;

var randomColor = () => {
    var r = Math.floor(Math.random() * 256)
    var g = Math.floor(Math.random() * 256) 
    var b = Math.floor(Math.random() * 256) 

        return `rgb(${r}, ${g}, ${b})`
}

var generateColor = (numColors) => {
    var listColor = [];
    for(var i = 0 ; i< numColors; i++){
        var ranColor = randomColor();
        listColor.push(ranColor);
    }
return listColor;
}


var colors = generateColor(6);


function pickColor()  {
    var random_num = Math.floor(Math.random() * colors.length);
    return colors[random_num];
}

var pickedColor = pickColor();


quizz.innerHTML = pickedColor;


// var pickedColor = colors[2]


var squares = document.querySelectorAll(".square");
// console.log(squares);

for(var i = 0;i < squares.length; i++){
    squares[i].style.backgroundColor = colors[i]
}

squares.forEach( (square) => {
    square.addEventListener("click",(event) =>{
        var clickedColor = event.target.style.backgroundColor
        
        
        

        if (clickedColor === pickedColor) {
            message.innerHTML = "IQ vô cực "
            message.style.color = "green"
            
        }
        else {
           
            message.innerHTML = "IQ 20"
            message.style.color = "red"
            
        }
        
    })
} )
var restart = () => {
    colors =generateColor(6);
    pickedColor = pickColor();
    quizz.innerHTML = pickedColor;
    message.innerHTML = "Doan xem";
    message.style.color = "white";
    for(var i = 0;i < squares.length; i++){
        squares[i].style.backgroundColor = colors[i]
    }

}

// var random = Math.floor(Math.random() * 256)
// console.log(random);
reset.addEventListener("click", () =>{
    restart();
})








    


