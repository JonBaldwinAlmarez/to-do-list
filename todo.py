"""To-Do List"""

TO_DO_LIST = []


def print_to_do():
    """Display the to-do list with indexes."""
    if not TO_DO_LIST:
        print("\n📝 Your to-do list is empty!\n")
    else:
        print("\n📝 Your To-Do List:")
        for index, task in enumerate(TO_DO_LIST):
            print(f"{index}. {task}")
        print()  # extra newline for spacing


def add_to_do():
    """Add a new task to the to-do list."""
    to_do = input("Enter what to do: ").strip()
    if to_do:
        TO_DO_LIST.append(to_do)
        print(f"✅ Added: {to_do}\n")
    else:
        print("⚠️ You didn't enter anything!\n")


def delete_to_do():
    """Delete a task by index."""
    print_to_do()

    if not TO_DO_LIST:
        return  # stop if list is empty

    try:
        index = int(input("Enter the index of the task to delete: "))
        if 0 <= index < len(TO_DO_LIST):
            removed = TO_DO_LIST.pop(index)
            print(f"🗑️ Deleted: {removed}\n")
        else:
            print("❌ Invalid index!\n")
    except ValueError:
        print("⚠️ Please enter a valid number!\n")


def main():
    """Main loop for the to-do list app."""
    while True:
        print("====== TO-DO LIST MENU ======")
        print("1️⃣  Add to-do")
        print("2️⃣  Delete to-do")
        print("3️⃣  Show to-do list")
        print("4️⃣  Exit")

        choice = input("Enter your choice (1–4): ").strip()

        match choice:
            case "1":
                add_to_do()
            case "2":
                delete_to_do()
            case "3":
                print_to_do()
            case "4":
                print("👋 Goodbye!")
                break
            case _:
                print("❌ Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
