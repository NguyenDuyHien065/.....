
shop_list = ["T-Shirt" , "Sweater"]


while True :
    command = input("\nWelcome to our shop , what do you want (C , R , U , D)")

    if command == "R" or command =="r":
        print("Our items :" , end=' ' )

    elif command == "C" or command == "c":
        items_to_add = input("Enter new items")
        shop_list.append(items_to_add)
    elif command == "U" or command == "u":
        position = int(input("Update position? "))
        update = position - 1
        shop_list.pop(update)
        shop_list.insert(update, input("New item? "))
        print("Our items:",end=" ")
    elif command == "d" or command == "D":
        delete = int(input("Delete position :"))
        del shop_list[delete-1]
    else :
        print ("Error . Please try gain !!!")
    for i in shop_list:
        print(i, end=" ")





