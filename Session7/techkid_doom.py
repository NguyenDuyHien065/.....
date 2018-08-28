player = {
    "NAME":"PROKILLER",
    "CLASS":"STUDENT",
    "HP":150,
    "STR":25,

    "DEF":10,

    "LVL":3,
}
while True :
    print("*"*10)
    print("Viết 'stats' để xem chỉ số bản thân hoặc viết 'play' để chơi")
    cmd = input("Your command:")
    if cmd == "stats":
        print("Name :", player["NAME"])
        print("CLASS:", player["CLASS"])
        print("HP", player["HP"])
        print("STR:", player["STR"])
        print("DEF:", player["DEF"])
        print("LEVEL:", player["LVL"])
    elif cmd == "play":
        print("Bạn là sát thủ và bạn đang chọn 1 nơi để giết người")
        print("Chọn địa điểm để giết người")
        print("1.Trường học")
        print("2.Techkids")
        print("3.Gia nhập SUICIDE SQUAD để Tự Tử tập thể")
        option = input("Chọn địa điểm để giết người")
        if option == "1" :
            print("Do bạn lướt  nhanh như Yashou nên bị rơi xuống hố tử thần ngay trước trường học ")
            print("YOU DEAD , SUCKER")
        elif option == "2" :
            print("Bạn đang đứng trước số 22 đường Thành Công")
            print("Bạn đi thang máy lên tầng 5 và đi bộ lên tầng 6")
            print("Vừa bước chân vào Techkid ")
            print("Bước vào Techkid , bạn gặp chị San")
            print("Tiếp theo bạn sẽ làm gì ?")
            print("1.Lao vào giết")
            print("2.Tán tỉnh ")
            print("3.Mặc kệ")
            option = input("Lựa chọn của bạn :")
            if option == "1":
                san = {
                    "NAME":"Chị San",
                    "CLASS":"Quản Trò",
                    "HP": 20,
                    "STR": 5,

                    "DEF": 5,

                    "LVL": 1,

                }
                print("NAME:",san["NAME"])
                print("CLASS:",san["CLASS"])
                print("HP:",san["HP"])
                print("STR:",san["STR"])

                print("DEF:",san["DEF"])

                print("LVL:",san["LVL"])
                print(".....")
                print("Prokiller vs chị San")
                print("Trận đấu bắt đầu")
                damage = player["STR"]-san["DEF"]
                san["HP"]=san["HP"]-damage
                print ("Bạn tung 1 cước vào mặt đối phương")
                print("Đối phương vừa mất",damage,"HP")
                print("HP hiện tại của chị San:",san["HP"],"HP")
                print("K.O")
                print("Bạn đã giết chị San")
                print("Bạn nhân được vũ khí mới : Kiếm Assassin X")
                player["STR"]= 40
                print("Bạn được cộng : 15 STR")
                print("STR hiện tại của bạn:",player["STR"])
                print(".............")
                print("Bạn đi sâu vào căn cứ Techkids")
                print("Bỗng nhiên...")
                print("Bạn gặp anh Huy đang ăn bimbim , xem phim người khác đang ăn 1 gói bimbim khác")
                huy = {
                    "NAME": "Huy Hihi",
                    "CLASS": "Hihi",
                    "HP": 90,
                    "STR": 20,

                    "DEF": 10,

                    "LVL": 2,
                }
                print("NAME:",huy["NAME"])
                print("CLASS:",huy["CLASS"])
                print("HP:",huy["HP"])
                print("STR:",huy["STR"])

                print("DEF:",huy["DEF"])

                print("LVL:",huy["LVL"])




                print("Bạn sẽ:")
                print("1.Attack")
                print("2.Run")
                option = input("Lựa chọn của bạn :")
                if option =="1":
                    print("Cuộc chiến giữa 2 người đàn ông chuẩn bị diễn ra")
                    print("Xin quý vị hãy ổn định chỗ ngồi")
                    print("PROKILLER vs Huy")
                    for i in range(2):
                        damage = player["STR"] - huy["DEF"]
                        huy["HP"] = huy["HP"] - damage
                        damage2= huy["STR"] - player["DEF"]
                        player["HP"] = player["HP"] - damage2

                        print("Bạn sử dụng kiếm Assassin X chém 1 nhát vào anh Huy")
                        print("Huy mất:",damage,"HP)
                        print("HP hiện tại của anh Huy:", huy["HP"],"HP)
                        print("Mặc dù bị chém , anh Huy vãn cười hihi")
                        print("Ngay lập tức đối phương sử dụng 1 cú đấm vô cùng binh thường vào bạn!!!")
                        print("Bạn mất",damage2,"HP")
                        print("HP hiện tại của bạn:",player["HP"],"HP")
                    damage = player["STR"] - huy["DEF"]
                    huy["HP"] = huy["HP"] - damage
                    damage2 = huy["STR"] - player["DEF"]
                    player["HP"] = player["HP"] - damage2

                    print("Bạn sử dụng kiếm Assassin X chém 1 nhát vào anh Huy")
                    print("Huy mất:", damage)
                    print("HP hiện tại của anh Huy:", huy["HP"])
                    print("K.O")
                    print("Huy has been slained")
                    print("Bạn nhận được 20.000 Đ trong ví của anh Huy ")
                    print("Bỗng...")
                    print("Từ phía xa xa , Đức-Huy's best friend ,nhì thấy người bạn của mình đang nằm trên vũng máu , 2 tay buông thõng ")
                    print("Đức đến gần thì thấy vũng máu là ....")
                    print(".....Sốt cà chua mà anh Huy làm đổ trong trận chiến long trần nhà lở sàn gỗ với bạn tại Techkids")
                    print("Vô cùng bức xúc trước sự ra đi đột ngột của người bạn , Đức huy động toàn bộ sức mạnh và nội tại mình có để quyết chiến với PROKILLER(Bạn)")
                    duc = {
                        "NAME": "Đức Hihi",
                        "CLASS": "Hihi",
                        "HP": 150,
                        "STR": 30,

                        "DEF": 10,

                        "LVL": 5,
                    }
                    print("NAME:", duc["NAME"])
                    print("CLASS:", duc["CLASS"])
                    print("HP:", duc["HP"])
                    print("STR:", duc["STR"])

                    print("DEF:", duc["DEF"])

                    print("LVL:", duc["LVL"])
                    print("Bạn chọn ?")
                    print("1.Tha , không chấp con nít")
                    print("2.Chiến tiếp")
                    option = input("Lựa chọn của bạn :")

                    if option == "1":
                        print("Đức sử dụng nội tại 'hihi*100' khiến bạn bị thôi miên và fall in love with your opponent ")
                        print("Và 2 người sống không hạnh phúc mãi mãi về sau :))")
                        print("=> YOU LOSE")
                    elif option =="2":
                        for i in range(4):
                            damage = player["STR"] - duc["DEF"]
                            duc["HP"] = duc["HP"] - damage
                            damage2 = duc["STR"] - player["DEF"]
                            player["HP"] = player["HP"] - damage2
                            print("Bạn sử dụng kiếm Assassin X chém 1 nhát vô cùng đau đớn vào anh Đức")
                            print("Đức mất:", damage)
                            print("HP hiện tại của anh Đức:", duc["HP"])
                            print("Mặc dù bị chém trọng thương  song Đức đã dùng máy tính đập vào đầu bạn")
                            duc["STR"] = duc["STR"]+5
                            print("Kẻ địch tăng:5 STR")

                            print("Sức tấn công hiện tại của địch:",duc["STR"])
                            print("Ngay lập tức đối phương sử dụng 1 cú đấm vô cùng binh thường vào bạn!!!")
                            print("Bạn mất", damage2, "HP")
                            print("HP hiện tại của bạn:", player["HP"], "HP")
                        damage = player["STR"] - duc["DEF"]
                        duc["HP"] = duc["HP"] - damage
                        print("Bạn vừa tung cú chém kết liễu đối phương")
                        print("Kẻ địch mất:", damage,"HP)
                        print("HP hiện tại của địch:",duc["HP"],"HP")
                        print("Đối phương đã gục")
                        print("Bạn nhận được vũ khí mới: Máy tính")
                        player["LVL"]= 10
                        player["HP"]=200
                        player["STR"]= 50
                        print("Level up:",player["LVL"])
                        print("HP up:", player["HP"])
                        print("Strengh up:", player["STR"])
                        print("\nChiến thắng")
                    else:
                        print("Không hiểu tiếng người à !")
                elif option == "2":
                    print("Bạn chạy nhầm vào chỗ ngồi của anh Huy")
                    print("Cả 2 trao cho nhau nụ hôn nồng cháy")
                    player["HP"]=0
                    huy["HP"]=0
                    print("Máu của bạn hiện tại:",player["HP"],"HP")
                    print("\nMáu của Huy hiện tại:",huy["HP"],"HP")
                    print('Double K.O')
                    print("Thua")
                else:
                    print("Không hiểu tiếng người à !")






            elif option =="2":
                print("Chị San tung 1 cú đá vào 'tr*m'của bạn")
                player["HP"]=0
                print("Máu hiện tại của bạn:",player["HP"],"HP")
                print("Này thì dại gái")
            elif option =="3":
                print("Bạn không đủ tiêu chuẩn làm sát thủ")
                print("END GAME")
            else:
                print("Không hiểu tiếng người à !")





        elif option =="3":
            print("Bạn đã gia nhập SUICIDE SQUAD và kết liễu cuộc đời mình")
            print("GAME OVER")
        else :
            print("Không biết đọc à !")
    else:
        print("Không hiểu tiếng người à !")
