""" To do list"""

TO_DO_LIST = []

def delete_to_do():
    print_to_do()
    print("\n")

    index = int(input("Enter the index of the task to delete"))
    if 0 <= index <= len(TO_DO_LIST):
        removed = TO_DO_LIST.pop(index)
        print(f"Deleted {removed} \n")
    
    else:
        print("Invalid index")

def add_to_do():
    to_do = input("Enter what to do:    ")
    TO_DO_LIST.append(to_do)
    print(TO_DO_LIST)

def print_to_do():
    print("\n Your To-Do List:")
    for index, task in enumerate(TO_DO_LIST):
            print(f"{index}. {task}")
    print()

def main():
    while True:

        verification = input("Do you have something to do?  Y / N:  ")
        
        if verification == "Y":
            print("press 1 to add to do")
            print("press 2 to delete to do")
            print("press 3 to print to do")

            answer = input("Please enter answer:    ")

            match answer:
                case "1":
                    add_to_do()
                case "2":
                    delete_to_do()
                case "3":
                    print_to_do()
        
        else:
            return True

main()