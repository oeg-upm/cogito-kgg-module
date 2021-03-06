import subprocess
import sys
sys.stdout.flush()

class Triple_Store_Controller:

    def __init__(self, uuid, file_name, container_uuid, triple_store_url, sparql_endpoint_url):
        self.uuid = uuid
        self.file_name = file_name
        self.container_uuid = container_uuid
        self.sparql_endpoint = sparql_endpoint_url
        self.triple_store_url = triple_store_url

    def delete_graph(self):
        proc = subprocess.Popen(["curl", 
        "--digest", 
        "--verbose", 
        "--user", 
        "dba:mysecret", 
        "--url", 
        self.triple_store_url + "sparql-graph-crud-auth?graph-uri=" + self.triple_store_url + self.uuid, 
        "-X", 
        "DELETE"], # Change middle with real file name
        shell=False, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)

        (out, err) = proc.communicate()
        lastCode = str(err).split('HTTP/1.1 ')[-1].split(" ")[0]

        if lastCode == "200":
            print(["Deleted", 200])
        else:
            print(["You did something wrong", 500])


    def save_graph(self, raw_graph):

        # Create graph file
        path_to_file = "Files_Storage/" + self.file_name + ".ttl"
        f = open(path_to_file, "w")
        f.write(raw_graph)
        f.close()

        proc = subprocess.Popen(["curl", 
        "--digest", 
        "--verbose", 
        "--user", 
        "dba:mysecret", 
        "--url", 
        self.triple_store_url + "sparql-graph-crud-auth?graph-uri=" + self.triple_store_url + self.uuid, 
        "-T", 
        "Files_Storage/" + self.file_name + ".ttl"],
        shell=False, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)

        (out, err) = proc.communicate()
        lastCode = str(err).split('HTTP/1.1 ')[-1].split(" ")[0]

        if lastCode == "200":
            print(["Updated Graph or Existing Graph", 200])
        elif lastCode == "201":
            print(["Created Graph", 201])
        elif lastCode == "401":
            print(["Error with Authorization", 401])
        else:
            print(["You did something wrong", 500])

