import requests
import os


class Generate_IDF_Graph:
    def __init__(self, file_name, file_raw, format): # file = temp.name
        self.url = "https://kgg.openmetrics.eu/"
        self.url_post = "https://kgg.openmetrics.eu/upload"
        self.url_get = "https://kgg.openmetrics.eu/download"
        self.file_format = format
        self.file_raw = file_raw
        self.file_name = file_name
        self.files = []
        self.payload = {}
        self.raw_graph = ""


    def generate_graph(self):
        s = requests.Session()
        s.get(self.url, verify=False)

        headers_post = {
            'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
        }
        headers_get = {
            'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
        }

        response_post = requests.post(self.url_post, headers=headers_post, data=self.payload, files=self.files, verify=False)
        response_get = requests.get(self.url_get, headers=headers_get, data=self.payload, verify=False)

        self.raw_graph = response_get.text

    def make_execution(self):
        file_path = "Files_Storage/" + self.file_name + "." + self.file_format
        with open(file_path, "w") as f:
            f.write(self.file_raw)
            f.close()
        try:
            self.files = [('file',(file_path,open(file_path, 'rb'),'application/octet-stream'))]
            self.generate_graph()
            #graph = open("Files_Storage/Bloque A.ttl", "r")
            #self.raw_graph = graph.read()
        finally:
            os.remove(file_path)