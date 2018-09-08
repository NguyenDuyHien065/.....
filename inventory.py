player = {
    "NAME": "AOV",
    "CLASS": "HACKER",                     #Rất quan trọng
    "HP":60,
    "STR":7,
    "AGI":1,
    "DEF":5,
    "LVL":1,
    "LUCK":10,
}
org = {
    "NAME": "Org guard",
    "STR": 6,
    "DEF": 2,
    "HP": 6,
    "LUCK":6,
}
print ("Here are your weapon")
steal_gaunlet={
    "NAME":"STEAL GAUNLET",
    "HP":10,
    "AGI":-5,
    "STA":-3,
    "LUCK":1,


}

bronze_shield = {
    "NAME":"BRONZE SHIELD",
    "HP":10,
    "AGI":-2,
}


golden_stick = {
    "NAME":"GOLDEN STICK",
    "AGI":15,
    "HP":20,
    "STR":100,

}




def show_item(game_item):


    print("*"*15)
    for key, value in game_item.items():
        print("*",key, ":", value)

    print("*" * 15)


inventory = [steal_gaunlet,bronze_shield,golden_stick]
for item in inventory:
    show_item(item)
# show_item(steal_gaunlet)
#
# show_item(bronze_shield)


def combat(attacker,defender):
    print(attacker["NAME"],"is beating",defender["NAME"])
    show_item(player)
    show_item(org)


    damage = attacker["STR"]-defender["DEF"]
    if damage > 0 :
        defender["HP"]-= damage
        print(defender["NAME"],"lost",abs(damage),"HP")

    else:
        attacker["HP"]-= abs(damage)
        print(attacker["NAME"],"lost",damage,"HP")

while org["HP"]>0 and player["HP"]>0:

    combat(player,org)
    combat (org,player)
while True:
    combat(player,org)

    show_item(player)
    show_item(org)
    if org ["HP"]<= 0  :
        print("Victory")
        break


    elif player["HP"] <= 0  :
        print("Defeated")
        break

    combat(org, player)
    show_item(player)
    show_item(org)

    if org ["HP"]<= 0  :
        print("Victory")
        break


    elif player["HP"] <= 0  :
        print("Defeated")
        break
