//  var input = prompt("New account:")
//  var input2= prompt("Your password include only number , no word are allowed","\nNew password:")
//  var input3 = prompt("Re-enter the password:")
 while (true) {
    var input = prompt("New account:")
    var input2= prompt("Your password include only number , no word are allowed.\nNew password:")
    var input3 = prompt("Re-enter the password:")
    if (input2 === input3){
        break;
        

     }
    else{
         console.log("Wrong password , try again");
         
        
    }
    
}

 var input4 = prompt("Dont't need to write '@gmail.com'.\nYour email:" )
 console.log(input);
 console.log(input2);
 console.log(input4 ,  "@gmail.com" );
