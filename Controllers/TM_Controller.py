import requests
import os


class TM_Controller:

    def __init__(self, json_info):
        self.url = "http://localhost:8080"
        self.file_uuid = json_info['uuid']
        self.container_uuid = json_info['container']
        self.graph_file_path = ""
        self.file_name = json_info['name']
        self.file_format = json_info['format']
        self.container_TD = "https://wothive.linkeddata.es/api/things/" + self.container_uuid
        self.file_raw = ""


    def retrieve_file(self): # Retrieve file from the container
        response = requests.get(self.url + "/containers/" + self.container_uuid + "/files/" + self.file_uuid)
        self.file_raw = response.text


    def add_graph_file(self): # Add graph file to the container
        graph_file_path = "Files_Storage/" + self.file_name + ".ttl"
                
        url = self.url + "/containers/" + self.container_uuid + "/files/" + self.file_uuid
        files=[
            ('file',(self.file_name + ".ttl",open(graph_file_path,'rb'),'application/octet-stream'))
        ]
        headers = {}
        payload = {}
        print(url)
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        print(response.text)
        os.remove(graph_file_path)

    def create_graph_TDs(self):
        pass