
from neat_globals import *



class Connection:

    def __init__(self, input_node_id, output_node_id, weight, enabled):
        self.input_node_id = input_node_id
        self.output_node_id = output_node_id
        self.weight = weight
        self.enabled = enabled
        self.id = get_next_connection_id()

def create_random_initial_connections(nodes):
    connection_list = list()

    return connection_list

