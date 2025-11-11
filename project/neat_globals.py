import ast

activation_function_list = ("ReLu","Sigmoid","Tanh","none")
globals_dict = dict()

def get_next_node_id():
    next_node_id = globals_dict['next_node_id']
    globals_dict['next_node_id'] += 1
    write_globals_file()
    return next_node_id

def get_next_connection_id():
    next_connection_id = globals_dict['next_connection_id']
    globals_dict['next_connection_id'] += 1
    write_globals_file()
    return next_connection_id

def write_globals_file():
    file = open('GLOBAL_VARIABLES.txt', 'w')
    file.write(str(globals_dict))
    return

def read_globals_file():
    file = open("GLOBAL_VARIABLES.txt", 'r')
    global globals_dict
    globals_dict = ast.literal_eval(file.read())
    file.close()

def init_globals_dict():
    global globals_dict
    globals_dict['next_node_id'] = 0
    globals_dict['next_connection_id'] = 0
    write_globals_file()


read_globals_file()