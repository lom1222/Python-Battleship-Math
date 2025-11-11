
from neat_globals import *



class Node:

    def __init__(self, node_type, activation_function="ReLu", bias_value=0):
        self.node_type = node_type
        self.activation_function = activation_function
        self.bias_value = bias_value
        self.id = get_next_node_id()
        self.value = 0



def create_node_list(num_nodes, node_type, activation_function="ReLu", bias_value=0):
    node_list = list()
    for _ in range(num_nodes):
        node_list.append(Node(node_type=node_type, activation_function=activation_function, bias_value=bias_value))
    return node_list