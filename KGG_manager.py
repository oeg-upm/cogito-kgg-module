from sseclient import SSEClient
from Services.KGG_manager_service import evaluator
import configparser
import sys
sys.stdout.flush()


def kgg_manager():

    parser = configparser.ConfigParser()
    parser.read('kgg_manager.config')
    sse_url = parser.get("config","sse_url")

    url = sse_url
    messages = SSEClient(url)
    
    for msg in messages:
        msg_list = msg.data.split(';')
        if msg_list[0] == "file": # If not file in event pass
            print("Creating/Deleting")
            evaluator(msg_list, parser)
        else:
            print("Not file event")
            pass
            # Not a file
        

if __name__ == '__main__':
    while True:
        try:
            print("KGG Process Started")
            kgg_manager()
            print("KGG Process Ended")
        except:
            print("Restarting SSE Client")
            pass



# {-,"name":"Bloque A","format":"ifc","description":"https://wothive.linkeddata.es/api/things/uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","container":"uuid:container:20c438e2-86d1-4b3e-8ef3-236b97f307e8"}

# {"uuid":"uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","name":"Bloque A","format":"ifc","description":"https://wothive.linkeddata.es/api/things/uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","container":"uuid:container:20c438e2-86d1-4b3e-8ef3-236b97f307e8"}