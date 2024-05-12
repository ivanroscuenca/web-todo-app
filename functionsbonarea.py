FILEPATH = 'todos/todosbonarea.txt'


def get_todos(filepath=FILEPATH):
    """
  Read a text file and return a list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items in the file """
    with open(filepath, 'w') as file_local2:
        file_local2.writelines(todos_arg)


if __name__ == "__main":
    print("hello")
    print(get_todos())
