import json

class Json:
    def read(filename):
        with open(filename,"r") as file:
            return json.load(file)     
    def write(filename,dictionary:dict):
        json_object = json.dumps(dictionary, indent = 4)
        open(filename,"w").write(json_object)     