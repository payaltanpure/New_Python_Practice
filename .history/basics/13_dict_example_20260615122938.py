# Shopping Mart Management System

shop = {
    "cloths": {
        "tshirts": 100,
        "pants": 700
    },
    "electronics": {
        "laptop": 8000,
        "mobile": 1000,
        "washing_machine": 6000
    }
}

while True:
    print("\n===== Shopping Mart =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Total Bill")
    print("6. Search Item")
    print("7. Exit")

    ip = int(input("Enter your choice: "))

    # =========================
    # ADD ITEM
    # =========================
    if ip == 1:

        category = input("Enter category name: ")
        item = input("Enter item name: ")
        price = int(input("Enter price: "))

        # CHANGED CODE
        # Earlier:
        # shop.update({category:{item:price}})
        #
        # Problem:
        # If category already existed, all old items were deleted.
        #
        # Example:
        # electronics -> laptop,mobile
        # Adding TV would remove laptop and mobile.
        #
        # Solution:
        # Check whether category already exists.

        if category in shop:
            shop[category][item] = price
        else:
            shop[category] = {item: price}

        print("Item added successfully")

    # =========================
    # VIEW ITEMS
    # =========================
    elif ip == 2:

        print("\nAvailable Items:")

        for category, value in shop.items():
            print("\nCategory:", category)

            for item_name, item_price in value.items():
                print(item_name, ":", item_price)

    # =========================
    # UPDATE ITEM
    # =========================
    elif ip == 3:

        update_cat = input("Enter category to update: ")
        update_item = input("Enter item to update: ")

        # CHANGED CODE
        # Earlier:
        # if update_item in shop[update_cat]
        #
        # Problem:
        # If category doesn't exist, program crashes with KeyError.
        #
        # Solution:
        # First check category exists.

        if update_cat in shop:

            if update_item in shop[update_cat]:

                update_price = int(input("Enter new price: "))
                shop[update_cat][update_item] = update_price

                print("Data updated successfully")

            else:
                print("Item not found")

        else:
            print("Category not found")

    # =========================
    # DELETE ITEM / CATEGORY
    # =========================
    elif ip == 4:

        print("\n1. Delete Category")
        print("2. Delete Item")

        ch = int(input("Enter choice: "))

        # DELETE CATEGORY
        if ch == 1:

            category = input("Enter category name: ")

            if category in shop:
                del shop[category]

                # Alternative:
                # shop.pop(category)

                print("Category deleted successfully")

            else:
                print("Category not found")

        # DELETE ITEM
        elif ch == 2:

            category = input("Enter category name: ")
            item = input("Enter item name: ")

            # CHANGED CODE
            # Earlier:
            # if category in shop and item in shop
            #
            # Problem:
            # item in shop checks only top-level keys.
            #
            # Example:
            # laptop is inside electronics
            # so item in shop returns False.
            #
            # Solution:
            # Check item inside selected category.

            if category in shop and item in shop[category]:

                del shop[category][item]

                print("Item deleted successfully")

            else:
                print("Category or Item not found")

    # =========================
    # TOTAL BILL
    # =========================
    elif ip == 5:

        total = 0

        while True:

            category = input("Enter category name: ")
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))

            # CHANGED CODE
            # Added category existence check.
            #
            # Earlier:
            # shop[category]
            #
            # Problem:
            # Wrong category causes KeyError.

            if category in shop and item in shop[category]:

                price = shop[category][item]

                # CHANGED CODE
                # Earlier:
                # total += price*qty
                # print(total)
                #
                # Problem:
                # Displayed running total instead of
                # item's actual amount.

                amount = price * qty
                total += amount

                print(
                    item,
                    ":",
                    qty,
                    "*",
                    price,
                    "=",
                    amount
                )

            else:
                print("Category or Item not found")

            choice = input("Do you want to continue (y/n): ")

            if choice.lower() == 'n':

                # CHANGED CODE
                # Added final bill display

                print("\nTotal Bill =", total)
                print("Thank You for Shopping!")

                break

#    search item

    elif ip==6:
        print("1.Search by category name")
        print("2.Search by item name")
        ch= int(input("Enter choice:"))
        if ch==1:
            category= input("Enter categroy to search:")
            if category in shop:
               for k, v in shop[category].items():
                   print(k,":", v)
        elif ch==2:
            category= input("Enter categroy to search:")
            item = input("Enter item name")
            if category in shop and item in shop[category]:
                for category in shop




    # =========================
    # EXIT
    # =========================
    elif ip == 7:

        print("Thank You! Visit Again.")
        break

    else:
        print("Invalid Choice")