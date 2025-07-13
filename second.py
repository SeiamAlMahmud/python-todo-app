def get_todos(filePath):
    with open(filePath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(filePath, todos_arg = 'todos.txt'):
    with open(filePath, 'w') as file:
        file.writelines(todos_arg)
write_todos('todos.txt','seiam')
todos = get_todos('todos.txt')
print(todos)