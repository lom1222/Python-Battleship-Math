
from project.neat_globals import *



class Node:

    def __init__(self, node_id, node_type, activation_function="ReLu", bias_value=0):
        self.node_type = node_type
        self.activation_function = activation_function
        self.bias_value = bias_value
        self.id = node_id

        self.value = 0

    def __json__(self):
        return {
            "node_type": self.node_type,
            "activation_function": self.activation_function,
            "bias_value": self.bias_value,
            "id": self.id,

            #"value": self.value
        }

    def load_from_json(self, json_string):

        return



def create_node_list(num_nodes, node_type, activation_function="ReLu", bias_value=0):
    node_list = dict()
    for _ in range(num_nodes):
        node_id = get_next_node_id()
        node_list[node_id] = Node(node_id=node_id, node_type=node_type,
                                  activation_function=activation_function,
                                  bias_value=bias_value)
    return node_list