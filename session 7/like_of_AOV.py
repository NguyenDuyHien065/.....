#player = ["AOV","Hacker",100, 7 ,1 , 8 ,2 ]
#{}:dictionary
#<key>:<value>
player = {
    "NAME": "AOV",
    "CLASS": "HACKER",                     #Rất quan trọng
    "HP":60,
    "STR":7,
    "AGI":1,
    "DEF":10,
    "LVL":1,
}
while True :
    print("*"*10)
    print("Viết 'stats' để xem chỉ số bản thân hoặc viết 'here' để chơi")
    cmd = input("Your command")
    if cmd == "stats":
        print("Name :", player["NAME"])
        print("CLASS:", player["CLASS"])
        print("HP", player["HP"])
        print("STR:", player["STR"])
        print("DEF:", player["DEF"])
        print("LEVEL:", player["LVL"])
    elif cmd == "here":
        print("Bạn đang ở trước cửa lâu đài")
        print("Bạn có 2 lựa chọn")
        print("1 . Về Techkids")
        print("2.Đi vào cánh rừng đối diện")
        option = input ("Lựa chọn của bạn ?")
        if option == "1":
            print("Xin lỗi , đã hết giờ làm việc")
            print("Nhập lại đi !!")
            print("Bạn có 2 lựa chọn")
            print("1 . Về Techkids")
            print("2.Đi vào cánh rừng đối diện")
            option = input("Lựa chọn của bạn ?")
            if option == "2":
                if option == "2":
                    print("Bạn đã bước vào dừng")
                    print("...")
                    print("Bạn thấy một bình thủy dịch ở trên mặt đất")
                    print("1.Bỏ qua")
                    print("2.Nhặt lên uống")
                    option = input("Lựa chọn của bạn ?")
                    if option == "1":
                        print("Tiếc quá")
                    elif option == "2":
                        player["HP"] = 100  # Rất quan trọng
                        print("Bạn đã được hồi phục hoàn toàn máu")

                        print("HP", player["HP"])

                    print("Bạn gặp 1 con Orc")
                    print("Bạn sẽ")
                    print("1 . Chạy trốn")
                    print("2 . Nấp vào hang đá bên cạnh")
                    print("3. Đánh")
                    option = input("Lựa chọn của bạn ?")
                    if option == "1":
                        print("Do bạn chạy quá chậm nên bạn bị Orc giết")
                    elif option == "2":
                        print("Con Orc không nhìn thấy bạn và bỏ đi")
                        print("Tuy nhiên , khi bạn quay lại nhìn vào hang thì thấy 1 đàn sói")
                    elif option == "3":
                        print("Chỉ số của Org:")
                        org = {"NAME": "Org guard",
                               "STR": 1,
                               "DEF": 2,
                               "HP": 6,

                               }
                        print("Name :", org["NAME"])

                        print("HP", org["HP"])
                        print("STR:", org["STR"])
                        print("DEF:", org["DEF"])
                        print("Con người và quái vật bắt đầu tiến vào'phang nhau', nhưng chỉ có 1 người sống sót")
                        print("HUMAN vs MONSTER")
                        damage = player["STR"] - org["DEF"]
                        org["HP"] = org["HP"] - damage
                        if damage > 0:
                            org["HP"] = org["HP"]
                            print("Bạn vừa đấm quái vật")
                            print("Org vừa mất", damage, "HP")
                            print("HP hiện tại của Org guard", end=' ')

                            print(org["HP"])
                            damage = player["STR"] - org["DEF"]
                            org["HP"] = org["HP"] - damage
                            print("Quái vật choang váng, không thể tung ra đòn tấn công")
                            print(" Chớp thời cơ , bạn tung 1 cú critical hit")
                            print("Org vừa mất", damage, "HP")

                            print("HP hiện tại của Org guard: ", org["HP"])
                            print("Bạn vừa hút máu thêm 4 HP từ org")
                            player["HP"] = player["HP"] + 4
                            print(player["HP"])
                            print("Monster has been defeated ")


        elif option == "2":
            print("Bạn đã bước vào dừng")
            print("...")
            print("Bạn thấy một bình thủy dịch ở trên mặt đất")
            print("1.Bỏ qua")
            print("2.Nhặt lên uống")
            option = input("Lựa chọn của bạn ?")




            if option == "1":
                print("Tiếc quá")
            elif option == "2":
                player ["HP"] = 100 #Rất quan trọng
                print("Bạn đã được hồi phục hoàn toàn máu")

                print("HP", player["HP"])

            print("Bạn gặp 1 con Orc")
            print("Bạn sẽ")
            print("1 . Chạy trốn")
            print("2 . Nấp vào hang đá bên cạnh")
            print ("3. Đánh")
            option = input ("Lựa chọn của bạn ?")
            if option == "1":
                print("Do bạn chạy quá chậm nên bạn bị Orc giết")
            elif option == "2":
                print("Con Orc không nhìn thấy bạn và bỏ đi")
                print ("Tuy nhiên , khi bạn quay lại nhìn vào hang thì thấy 1 đàn sói")
            elif option =="3":
                print ("Chỉ số của Org:")
                org = {"NAME":"Org guard",
                       "STR": 1,
                       "DEF": 2,
                       "HP":6,

                       }
                print("Name :", org["NAME"])

                print("HP", org["HP"])
                print("STR:", org["STR"])
                print("DEF:", org["DEF"])
                print("Con người và quái vật bắt đầu tiến vào'phang nhau', nhưng chỉ có 1 người sống sót")
                print("HUMAN vs MONSTER")
                damage = player["STR"] - org["DEF"]
                org["HP"] = org["HP"] - damage
                if damage > 0:

                    org["HP"]=org["HP"]
                    print("Bạn vừa đấm quái vật")
                    print("Org vừa mất", damage , "HP")
                    print("HP hiện tại của Org guard",end=' ')

                    print(org["HP"])
                    damage = player["STR"] - org["DEF"]
                    org["HP"] = org["HP"] - damage
                    print("Quái vật choang váng, không thể tung ra đòn tấn công")
                    print (" Chớp thời cơ , bạn tung 1 cú critical hit")
                    print("Org vừa mất", damage, "HP")

                    print("HP hiện tại của Org guard:",org["HP"])
                    print("Bạn vừa hút máu thêm 4 HP từ org")
                    player["HP"] = player["HP"] + 4
                    print("HP hiện tại:",player["HP"])
                    print("Monster has been defeated ")
                    print("YOU WIN")
                    print("P/s : Vì creator quá lười và vẫn còn phải làm bài tập về nhà của Techkid nên chúng ta sẽ END GAME tại đây ")
        else:
            print("Bạn quá óc chó để chơi game này")
    else :
        print("YOU DEAD")