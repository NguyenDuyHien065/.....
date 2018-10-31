dare = document.querySelector(".clean-mtop-mbot")
var dareQuest = [
    "Screamed 'I AM CRAZY' 3 times",
   
    "Spin around 30 times",
    "Drink 1 liter of water in 1 minute",
    "Smell a fart of any player",
    "Being hit by any player in 10 shots,",
    "Push up 20 times",
    "Performing a 'banana plantation' for 10 seconds",
    "Lemon in the mouth 15 seconds",
    "For men, make up for them.",
    "Drop one in the toilet and hand out the other",
    "Drop 5 ice cubes into pants",
    "Dance without music for 1 minute",
    "Take out your shirt for 5 minutes",
    "Lick the floor",
    "Licking your elbow",
    "Two tablespoons of mustard",
    "Drinking water and step on your hands at the same time",
    "Hold your nose + hold your breath for 45 seconds,",
    "Smell other player's socks for 15 seconds",
    
    "Drink unboiled water",
    "Other players will change your hairstyle",
    "Cry until your tear come out",
    "Tied hands + feet in the tree for 8 minutes,",
    "Sing a song",
    "Scream a ... a ... a and do not take a breath for 30 seconds,",
    "Run around the room 10 rounds",
    "Locked in the toilet for 2 minutes",
    "Wear five more shirts and wear them in 30 minutes,",
    "Wear five more pants and wear them in 25 minutes",
    "Spin around 5 times and then jump ropes 15 times",
    "Hug another player",
    "Dancing like a mad guy ",
    "Do a magic trick",
    "Tell a scary story",
    "Close your eyes for 15 minutes",
    "Flip the bottle until you succeed",
    "Count from 1 to 100",
    "Pretend to be a dog",
    "Do the robot moves",
    "Dance without the music for 90s",
    "Smell the rubbish for 10s",
    "Tell a joke",
    "Do some Math",
    "Bark like a dog",
    "Be other player's pet for 6 minutes",
    "Smell your own shoes for 15s"

    
    

];
var choiceRandom = () => {
    
    var index = Math.floor(Math.random() * dareQuest.length);
       
    return dareQuest[index];
}
var choiceRandomed = choiceRandom();
dare.innerHTML = choiceRandomed;

// var clicks = document.querySelectorAll(".click");
var clicks = document.querySelectorAll(".click2");
clicks.forEach(clicks => {
    clicks.addEventListener("click", (event) => {
        if (clicked === choiceRandomed) {
            document.querySelectorAll(".clean-mtop-mbot")
                
            }
        else {
                console.log(dareQuest);
                
               
               
                
            }
            
        })
    
    
});
var otherQuestion = () =>{
    var choiceRandomed = choiceRandom();
    dare.innerHTML = choiceRandomed;
    for (var i = 0;i < dareQuest.length; i++){
        dareQuest[i].style.backgroundColor = dareQuest[i];
        



}
}
// click.addEventListener("click",()=>{
//     otherQuestion();
    
//  })
     
    
        



