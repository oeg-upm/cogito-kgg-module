from sseclient import SSEClient
from Services.KGG_manager_service import evaluator


def kgg_manager():
    url = "http://localhost:8080/sse"
    messages = SSEClient(url)
    for msg in messages:
        msg_list = msg.data.split(';')
        if msg_list[0] == "file": # If not file in event pass
            #print(msg_list[2])
            evaluator(msg_list)
        else:
            pass
            #print("Not a file")
        

if __name__ == '__main__':
    kgg_manager()



# {"uuid":"uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","name":"Bloque A","format":"ifc","description":"https://wothive.linkeddata.es/api/things/uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","container":"uuid:container:20c438e2-86d1-4b3e-8ef3-236b97f307e8"}

# {"uuid":"uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","name":"Bloque A","format":"ifc","description":"https://wothive.linkeddata.es/api/things/uuid:file:13b5b406-4043-47f8-8eda-ad72947f88fe","container":"uuid:container:20c438e2-86d1-4b3e-8ef3-236b97f307e8"}