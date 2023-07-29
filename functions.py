def get_todos(filepath="todos.txt"):
    """ Return the items from a file. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

# print(help(get_todos))


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# __name__ is "main" when you run this, but "functions" when imported
if __name__ == "__main__":
    print("Hello")
    print(get_todos("todos.txt"))