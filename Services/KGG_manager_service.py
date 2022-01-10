import json
import sys
sys.path.append("..")
sys.stdout.flush()
from Controllers.TM_Controller import TM_Controller
from Controllers.Triple_Store_Controller import Triple_Store_Controller
from Controllers.Generate_IDF_Graph import Generate_IDF_Graph
from Services.Graph_generator_service import Graph_Generator


def evaluator(msg, parser):
    tm_controller = TM_Controller(json.loads(msg[2]), parser.get("config","thing_manager_url"))
    if msg[1] == "deleted":
        graph_controller = Triple_Store_Controller(tm_controller.file_uuid, tm_controller.file_name, tm_controller.container_uuid, parser.get("config","triple_store_url"), parser.get("config","sparql_endpoint_url"))
        graph_controller.delete_graph()
    elif msg[1] == "created":
        tm_controller.retrieve_file() # has file in raw data inside a variable (self.file_raw)

        if tm_controller.file_format == "ifc":
            idf_graph_generator = Generate_IDF_Graph(tm_controller.file_name, tm_controller.file_raw, tm_controller.file_format)
            idf_graph_generator.make_execution() # Execute Generate_IDF_Graph Controller to generate IDF graph if file is idf
            graph_controller = Triple_Store_Controller(tm_controller.file_uuid, tm_controller.file_name, tm_controller.container_uuid, parser.get("config","triple_store_url"), parser.get("config","sparql_endpoint_url"))
            graph_controller.save_graph(idf_graph_generator.raw_graph) # Store it in the same container as the original file
            tm_controller.add_graph_file()

        else:
            #Execute Helio
            graph_generator = Graph_Generator()
            graph_generator.generate_graph_helio()
            pass

    else:
        pass