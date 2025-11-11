import json



class CustomEncoder(json.JSONEncoder):

    def default(self, obj):
        from project.neat_agent import Agent
        from project.neat_connection import Connection
        from project.neat_node import Node

        custom_class_list = (Agent, Node, Connection)

        if isinstance(obj, custom_class_list):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)
