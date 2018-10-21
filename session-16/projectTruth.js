var truth = document.querySelector(".clean-mtop-mbot")
var truthQuest=[
    "Bạn xem phim XXX lần đầu tiên vào năm bao nhiêu tuổi ?",
    "Bạn đã có gấu chưa . Nếu rồi thì đã xoạc chưa ?",

    "Bạn đã từng hôn ai chưa ?",
    
    
    "Bạn có crush không ?",
    
    
    "Bạn đã từng nghĩ mình nên làm liều ?",
    
    "Đã bao giờ bạn thẩm du khi có bố mẹ ở nhà ?",
    "Kể về 1 lần nghịch ngu của bạn ?",
    "Kể về điều biến thái nhất bạn từng làm ?",
    "Bạn có muốn hấp diêm Crush không ?",
    
    "Bạn có muốn đấm GVCN không ?",
    "Kể lý do bạn thích crush ?",
    "Bạn có yêu Đảng và Tổ Quốc không ?",
    "Nếu được chửi GVCN thì bạn sẽ chửi như thế nào ?",
    "Lý do bạn mất gốc Hóa ?",
    
    "Có phải bạn rất biến thái ?"

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
        
    
        