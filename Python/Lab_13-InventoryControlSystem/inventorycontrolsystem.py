
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    
    print("=========================================")
    print("         INVENTORY CONTROL SYSTEM        ")
    print("=========================================")
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit\n")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        print("\n--- Current Inventory ---")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
        print() 
        
    elif choice == "2":
        new_item = input("Enter item name to add: ")
        inventory.append(new_item)
        print(f'[SUCCESS] "{new_item}" added to inventory.\n')
        
    elif choice == "3":
        remove_item = input("Enter item name to remove: ")
    
        if remove_item in inventory:
            inventory.remove(remove_item)
            print(f'[SUCCESS] "{remove_item}" removed from inventory.\n')
        else:
            print(f'[ERROR] "{remove_item}" not found in inventory.\n')
            
    elif choice == "4":
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
        print() 
        
    # 5. Exit
    elif choice == "5":
        print("\nThank you for using the Inventory Control System. Goodbye!")
        break 
        
    else:
        print("\n[ERROR] Invalid choice. Please select a valid option (1-5).\n")