shop={
    "cloths":{
        "tshirts":100,
        "pants":700
    },
    "electronics":
    {
        "laptop": 8000,
        "mobile":1000,
        "washing_machine":6000
    }
}

while True:
    print("Shopping Mart\n1.Add items\n2.View Item\n3.Update Item\n4.Delete Item\n5.Total Bill\n6.Exit\n")
    ip= int(input("Enter your choice:"))

    if ip==1:
        category= input("Enter category name:")
        item= input("Enter Item name:")
        price= int(input("Enter price:"))
        shop.update({category:{item:price}})
        print("Item added successfully")
    
    elif ip==2:
        for category , value in shop.items():
            print("Category is:", category)
            for item_name, item_price in value.items():
                print(item_name, ":", item_price)
    
    elif ip==3:
        update_cat= input("Enter category to update:")
        update_item= input("Enter item to update:")
        if update_item in shop[update_cat]:
           update_price= int(input("Enter price to update"))
           shop[update_cat][update_item]=update_price
           print("Data updated")
        else:
            print("Item not found")

    elif ip==4:
        print("1.Delete Category\n2.Delete Item")
        ch= int(input("ENter choice"))
        if ch==1:
            category= input("Enter category name")
            if category in shop:
                del shop[category]
                print("Category deleted")
            else:
                print("Category not found")
        elif ch==2:
            category= input("Enter category name")
            item = input("Enter item name:")
            if  category in shop :
                if item in shop:
                    del shop[category][item]
                    print("Item deleted")
                else:
                    print("item not found")
            else:
                print("Category not found")

            else:
                


    elif ip==6:
        break;

print(shop)