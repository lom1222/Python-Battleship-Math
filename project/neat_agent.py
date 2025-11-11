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

    def load_from_file(self,file_path):
        file = open(file_path, "r")
        self.load_from_json(json.load(file))
        file.close()

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

    def load_from_json(self, json_string):

        return

    def basic_setup(self):
        self.input_nodes.update(create_node_list(self.inputs, "INPUT", activation_function="none"))
        self.hidden_nodes.update(create_node_list(self.hidden, "HIDDEN"))
        self.output_nodes.update(create_node_list(self.outputs, "OUTPUT"))
        self.connections.update(create_initial_connections(self.input_nodes, self.hidden_nodes, self.output_nodes))


def create_base_agent(inputs = 1, outputs = 1, meta_generation="null", generation = 0):
    agent = Agent(inputs=inputs, outputs=outputs, meta_generation=meta_generation, generation=generation)
    agent.basic_setup()
    return agent

def get_file_path(meta_gen = "null", gen = 0, agent_id = 0):
    file_path = "agents/meta_gen_"+meta_gen+"/gen_"+str(gen)+"/agent_"+str(agent_id)+".json"
    return file_path


