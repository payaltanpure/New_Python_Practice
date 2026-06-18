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
        for cateogory , value in shop.items():
            print("Category is:", category)
            for item_name, item_price in value.items():
                print(item_name, ":", item_price)
    
    elif ip==6:
        break;

print(shop)