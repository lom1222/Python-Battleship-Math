import json
import os

from neat_node import *
from neat_connection import *


class Agent:

    def __init__(self, inputs=1, outputs=1, hidden_nodes=1, meta_generation="null", generation=0, agent_id=0):
        self.inputs = inputs
        self.outputs = outputs
        self.hidden_nodes = hidden_nodes
        self.meta_generation = meta_generation
        self.generation = generation
        self.agent_id = agent_id

        self.nodes = list()
        self.connections = list()


    def save(self):
        file_path = "agents/meta_gen_"+self.meta_generation+"/gen_"+str(self.generation)
        os.makedirs(file_path, exist_ok=True)
        file_path = file_path+"/agent_"+str(self.agent_id)+".json"
        with open(file_path, "w") as file:
            data  = self.__dict__
            json.dump(data, file, indent=4)
        file.close()

    def load_from_file(self,file_path):
        file = open(file_path, "r")
        self.__dict__ = json.load(file)
        file.close()

    def basic_setup(self):
        self.nodes.append(create_node_list(self.inputs, "INPUT"))
        self.nodes.append(create_node_list(self.hidden_nodes, "HIDDEN"))
        self.nodes.append(create_node_list(self.outputs, "OUTPUT"))

        self.connections.append(create_random_initial_connections(self.nodes))
        return


def create_base_agent():
    agent = Agent(inputs=100, outputs=100, meta_generation="A")
    agent.basic_setup()
    return agent

def get_file_path(meta_gen = "null", gen = 0, id = 0):
    file_path = "agents/meta_gen_"+meta_gen+"/gen_"+str(gen)+"/agent_"+str(id)+".json"
    return file_path


