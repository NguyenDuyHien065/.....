dare = document.querySelector(".clean-mtop-mbot")
var dareQuest = [

    "Scream my crush is ... and I want to do with her / him",
    "Kiss the lips of players of the opposite sex with you",
    "Perform three different 'sex posture' with one player",
    "Smell a random thing from other player",
    "Eat a teaspoon of mustard",
    
    "Being hit by a single player ",
    "Do the push-up 100 times",
    "Performing a 'banana plantation' for 120 seconds",
    "Mustard in one minute",
    "For men, makeup, and women delete the makeup",
    "Drop one item into the toilet and use the hand to grab it",
    "Fan dance for 1 minute",
    "Take off your pants for 5 minutes",
    "Lick the table",
    "Two tablespoons of mustard",
    "Call Crush and say 'I love you'",
    "Kiss the cheek or lips of the same sex player",
    "Put ice in the underpants",
    "Other players will edit your hairstyle",
    "Sexy dance for 1 minute",
    "Telling a joke that must make another player laugh",
    "Lick your partner's breasts",
    "Kiss someone upside down a.k.a. Spider-man style",
    "Give another player a sensual massage",
    "Do a cartwheel naked",
    "Re-enact your favorite porn",
    "Touch yourself a little faking getting a lot of pleasure",
    "Lick your partner's butt",
    "Lick your partner's belly",
    "Lick your partner's ear",
    "Have a slap bet with someone",
    "Make out with someone on camera",
    "Dance on a dance chosen by your friends",
    "Take a shot of vodka",
    "Tell everybody an embarrassing story about yourself",
    "Put toilet paper on your body in a mummy-like fashion",
    "Fake the sex noises",
    "Sing a song as if you were sick",
    "Sing a song with water in your mouth",
    "Drink a shot from between a girl's boobs",
    "Kiss a player",
    "Slap a player",
    "Repeat each of your sentences twice",
    "Kiss your way down someone's back or front",
    "Touch another player's boobs",
    "Go outside and kiss a complete stranger",
    "Whisper your dirtiest fantasy in your partner's ear",
    "Kiss your partner's cheek",
    "Kiss the first person to walk through the door (in or out)",
    "Caress his cheek, then his hand, then his neck",
    "Touch your partner's breasts/chest",
    "Remove your partner's underwear ",
    "Pole dancing in 1 minute",
    "Stand before your crush and say 'Be my girlfriend'",
    "Kiss your crush",
    "Touch your girlfriend's boobs",

    
    

    
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
// var otherQuestion = () =>{
//     var choiceRandomed = choiceRandom();
//     dare.innerHTML = choiceRandomed;
//     for (var i = 0;i < dareQuest.length; i++){
//         dareQuest[i].style.backgroundColor = dareQuest[i];
        



// }
// }