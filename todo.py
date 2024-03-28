todo_items = []

def add_item(item):
    todo_items.append(item)
def view_items():
    for i, item in enumerate(todo_items, 1):
        print(f"{i}. {item}")

def update_item(index, new_item):
    todo_items[index] = new_item

def delete_item(index):
    todo_items.pop(index)

def search_item(keyword):
    return [item for item in todo_items if keyword.lower() in item.lower()]

print("Welcome to To-Do List App!")
while True:
    print("\nOption\tDescription")
    print("1\tAdd an item")
    print("2\tView all items")
    print("3\tUpdate an item")
    print("4\tDelete an item")
    print("5\tSearch an item")
    print("6\tQuit\n")

    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please try again.")
        continue

    if user_choice == 1:
        new_item = input("Enter the new item to be added: ")
        add_item(new_item)
        print(f"Added {new_item} to the To-Do List.")

    elif user_choice == 2:
        view_items()

    elif user_choice == 3:
        try:
            index = int(input("Enter the index of the item to be updated: "))
            new_item = input("Enter the new item: ")
            update_item(index - 1, new_item)
            print(f"Updated item at index {index}.")
        except IndexError:
            print("Index out of range.")

    elif user_choice == 4:
        try:
            index = int(input("Enter the index of the item to be deleted: "))
            delete_item(index - 1)
            print(f"Deleted item at index {index}.")
        except IndexError:
            print("Index out of range.")

    elif user_choice == 5:
        keyword = input("Enter the keyword to search: ")
        matches = search_item(keyword)
        if len(matches) == 0:
            print("No matches found.")
        else:
            print("Matching Items:")
            for i, item in enumerate(matches, 1):
                print(f"{i}. {item}")

    elif user_choice == 6:
        print("Thanks for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")
