import random

from project.neat_globals import *



class Connection:

    # input_node and output_node must be a dict {id:node_id, type:node_type}
    def __init__(self, connection_id, input_node, output_node, weight=0, enabled=True):
        self.input_node = input_node
        self.output_node = output_node
        self.weight = weight
        self.enabled = enabled
        self.id = connection_id

    def __json__(self):
        return {
            "input_node" : {
                "id" : self.input_node[id],
                "type" : self.input_node[type]
            },
            "output_node" : {
                "id" : self.output_node[id],
                "type" : self.output_node[type]
            },
            "weight" : self.weight,
            "enabled" : self.enabled,
            "id" : self.id
        }

    def load_from_json(self, json_string):

        return

def create_initial_connections(input_nodes, hidden_nodes, output_nodes):
    connection_list = dict()
    hidden_node_ids = list(hidden_nodes.keys())
    for input_node_id in input_nodes:
        connection_id = get_next_connection_id()
        hidden_node_id = random.choice(hidden_node_ids)
        connection_list[connection_id] = Connection(connection_id=connection_id,
                                                    input_node={id: input_node_id, type: 'INPUT'},
                                                    output_node={id: hidden_node_id, type: 'HIDDEN'})
    for output_node_id in output_nodes:
        connection_id = get_next_connection_id()
        hidden_node_id = random.choice(hidden_node_ids)
        connection_list[connection_id] = Connection(connection_id=connection_id,
                                                    input_node={id: hidden_node_id, type: 'HIDDEN'},
                                                    output_node={id: output_node_id, type: 'OUTPUT'})
    return connection_list

