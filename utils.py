import os

def read_str_input(file_name: str) -> [str]:
    my_input = read_input(file_name)
    return list(map(lambda x: x.strip(), my_input))

def read_int_input(file_name: str) -> [int]:
    my_input = read_input(file_name)
    return list(map(lambda x: int(x), my_input))

def read_input(file_name: str) -> [str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file_name)
    with open(input_file) as f:
        my_input = f.readlines()
    return my_input

def print_grid(grid):
    for row in grid:
        print(row)
    print()
