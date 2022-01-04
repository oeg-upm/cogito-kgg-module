import json
import sys
sys.path.append("..")
from Controllers.TM_Controller import TM_Controller
from Controllers.Triple_Store_Controller import Triple_Store_Controller
from Controllers.Generate_IDF_Graph import Generate_IDF_Graph

def evaluator(msg):
    tm_controller = TM_Controller(json.loads(msg[2]))
    if msg[1] == "deleted":
        # Start
        # Execute Sparql query deleting Graph
        graph_controller = Triple_Store_Controller(tm_controller.file_uuid, tm_controller.file_name, tm_controller.container_uuid)
        graph_controller.delete_graph()
        # End
    elif msg[1] == "created":
        # Start
        tm_controller.retrieve_file() # has file in raw data inside a variable (self.file_raw)

        if tm_controller.file_format == "ifc":
            idf_graph_generator = Generate_IDF_Graph(tm_controller.file_name, tm_controller.file_raw, tm_controller.file_format)
            idf_graph_generator.make_execution() # Execute Generate_IDF_Graph Controller to generate IDF graph if file is idf
            #print(idf_graph_generator.raw_graph)
            graph_controller = Triple_Store_Controller(tm_controller.file_uuid, tm_controller.file_name, tm_controller.container_uuid)
            graph_controller.save_graph(idf_graph_generator.raw_graph) # Guardarlo en el mismo container del fichero del evento
            # generate TDs
            tm_controller.add_graph_file()
        # End
        else:
            #Execute Helio
            pass

    else:
        pass