
try:
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
except FileNotFoundError:
    todos = []

while True: 
    user_action = input("Type add, show, edit, remove or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            todos.append(todo)
            
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

        case 'edit':
            number = int(input("Number of the todo to edit: ")) - 1
            if 0 <= number < len(todos):
                new_todo = input("Enter new todo: ") + '\n'
                todos[number] = new_todo

                
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            else:
                print("Invalid todo number!")
        case 'remove':
            number = int(input("Number of the todo to remove: ")) - 1
            if 0 <= number < len(todos):
                removed = todos.pop(number)
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
                print(f"Todo '{removed.strip()}' removed.")
            else:
                print('Invalid todo number!')
        case 'exit':
            print("Exiting...")
            break

        case _:
            print("Unknown command. Please type add, show, edit or exit.")
