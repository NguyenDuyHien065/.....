var truth = document.querySelector(".clean-mtop-mbot")
var truthQuest=[
    "Bạn xem phim XXX lần đầu tiên vào năm bao nhiêu tuổi ?",
    "Bạn đã có gấu chưa . Nếu rồi thì đã hôn chưa ?",

    "Bạn đã từng hôn ai chưa ?",
    "Bạn đã hôn ai chưa ?",
    "Bạn có thẩm du thường xuyên không ?",
    "Bạn có crush không ?",
    "Bạn có thích Loli không ?",
    "Có phải bạn rất hứng thứ với các bé gái",
    "Bạn đã từng nghĩ mình nên làm liều ",
    "Có phải bạn chơi Yasuo rất ngu",
    "Đã bao giờ bạn thẩm du khi có bố mẹ ở nhà",
    "Kể về 1 lần nghịch ngu của bạn",
    "Kể về điều biến thái nhất bạn từng làm",
    "Bạn có muốn hấp diêm Crush không",
    "Bạn có dám solo Yasuo với Hiếu",
    "Bạn có muốn đấm GVCN không",
    "Kể lý do bạn thích crush",
    "Bạn có yêu Đảng và Tổ Quốc không",
    "Nếu được chửi GVCN thì bạn sẽ chưi như thế nào",
    "Lý do bạn mất gốc Hóa",
    "Bạn có muốn solo Yasuo với Hiếu không",
    "Có phải bạn rất biến thái"

]
var choiceRandom = () => {
    
    var index = Math.floor(Math.random() * truthQuest.length);
       
    return truthQuest[index];
}
var choiceRandomed = choiceRandom();
truth.innerHTML = choiceRandomed;

var clicks = document.querySelectorAll(".click");
// var clicks = document.querySelectorAll(".click2");
clicks.forEach(clicks => {
    clicks.addEventListener("click", (event) => {
        if (clicked === choiceRandomed) {
            document.querySelectorAll(".clean-mtop-mbot")
                
            }
        else {
                console.log(truthQuest);
                
               
               
                
            }
            
        })
    
    
});
var otherQuestion = () =>{
    var choiceRandomed = choiceRandom();
    truth.innerHTML = choiceRandomed;
    for (var i = 0;i < truthQuest.length; i++){
        truthQuest[i].style.backgroundColor = truthQuest[i];
        



}
}
reset.addEventListener("click",()=>{
    otherQuestion();
})
        
    
