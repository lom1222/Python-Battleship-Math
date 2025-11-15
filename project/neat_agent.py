import json
import os

from project.neat_node import *
from project.neat_connection import *
from custom_json import CustomEncoder

class Agent:

    def __init__(self, inputs=1, outputs=1, hidden=1, meta_generation="null", generation=0, agent_id=0, parents="ex-nihilo"):
        self.inputs = inputs
        self.outputs = outputs
        self.hidden = hidden
        self.meta_generation = meta_generation
        self.generation = generation
        self.agent_id = agent_id

        self.input_nodes = dict()
        self.hidden_nodes = dict()
        self.output_nodes = dict()
        self.connections = dict()

        self.fitness = 0
        self.processing_time = 0
        self.game_states_processed = 0

        self.parents = parents


    def save(self):

        file_path = "agents/meta_gen_"+self.meta_generation+"/gen_"+str(self.generation)
        os.makedirs(file_path, exist_ok=True)
        file_path = file_path+"/agent_"+str(self.agent_id)+".json"
        with open(file_path, "w") as file:
            data  = self.__json__()
            json.dump(data, file, cls=CustomEncoder, indent=4)
        file.close()
        return file_path

    def load_from_file(self,file_path):
        file = open(file_path, "r")
        json_string = json.load(file)
        file.close()

        self.inputs = json_string["inputs"]
        self.outputs = json_string["outputs"]
        self.hidden = json_string["hidden"]
        self.meta_generation = json_string["meta_generation"]
        self.generation = json_string["generation"]
        self.agent_id = json_string["agent_id"]

        self.input_nodes = load_nodes(json_string["input_nodes"])
        self.hidden_nodes = load_nodes(json_string["hidden_nodes"])
        self.output_nodes = load_nodes(json_string["output_nodes"])
        self.connections = load_connections(json_string["connections"])

        self.fitness = json_string["fitness"]
        self.processing_time = json_string["processing_time"]
        self.game_states_processed = json_string["game_states_processed"]

        self.parents = json_string["parents"]

    def __json__(self):
        return {
            "inputs" : self.inputs,
            "outputs" : self.outputs,
            "hidden" : self.hidden,
            "meta_generation" : self.meta_generation,
            "generation" : self.generation,
            "agent_id" : self.agent_id,

            "fitness": self.fitness,
            "processing_time": self.processing_time,
            "game_states_processed": self.game_states_processed,

            "parents": self.parents,

            "input_nodes" : json.loads(json.dumps(self.input_nodes, cls=CustomEncoder, indent=4)),
            "hidden_nodes" : json.loads(json.dumps(self.hidden_nodes, cls=CustomEncoder, indent=4)),
            "output_nodes" : json.loads(json.dumps(self.output_nodes, cls=CustomEncoder, indent=4)),
            "connections" : json.loads(json.dumps(self.connections, cls=CustomEncoder, indent=4)),
        }

    def basic_setup(self):
        self.input_nodes.update(create_node_list(self.inputs, "INPUT", activation_function="none"))
        self.hidden_nodes.update(create_node_list(self.hidden, "HIDDEN"))
        self.output_nodes.update(create_node_list(self.outputs, "OUTPUT"))
        self.connections.update(create_initial_connections(self.input_nodes, self.hidden_nodes, self.output_nodes))


def get_file_path(meta_gen = "null", gen = 0, agent_id = 0):
    file_path = "agents/meta_gen_"+meta_gen+"/gen_"+str(gen)+"/agent_"+str(agent_id)+".json"
    return file_path


