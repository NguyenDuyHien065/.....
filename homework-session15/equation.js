var input = prompt("Equation ax^2 + bx +  c = 0\na = ")
var input2 = prompt("b =")
var input3 = prompt("c =")

var delta = input2**2 - 4 * input * input3
if (delta > 0){
    console.log("Phương trình có 2 nghiệm phân biệt");
    var x1 = -input2 /2/input + Math.sqrt(delta) / 2 /input
    var x2 = -input2 /2/input - Math.sqrt(delta) /2 / input
    console.log("x1 =",x1);
    console.log("x2 =",x2);
    
    
}   
else if (delta === 0 ){
    console.log("Phương trình có nghiệm kép");
    var x1 = -input2 /2/input + Math.sqrt(delta) / 2 /input
    console.log("x1 = x2 =",x1);
    


    
}
else{
    console.log("Phương trình vô nghiệm");
    
}



