import json

class Parser:
    def __init__(self, result, info):
        self.result = result
        self.info = info

    def addInfo(self, tag, pattern, response):
        for res in self.result:
            if res["tag"] == tag:
                for field in res:
                    if field == "patterns":
                        if not (pattern == "" or tag == "_"):
                            res[field].append(pattern)
                    elif field == "responses":
                        if not (response == "" or tag == "_"):
                            res[field].append(response)
    
    def removeDuplicates(self, array):
        return list(set(array))

    def start(self):
        for intent in self.info:
            tag = intent['Intent'].lower().replace(" ", "_") # replace blanckspace for underscore and lowercase tag
            result["intents"].append(
                {
                "tag": tag,
                    "patterns": [""],
                    "responses": [""],
                    "context": [""] 
                }
            )
        unique = { each['tag'] : each for each in self.result["intents"] }.values() # remove duplicates
        self.result = unique
        
        for intent in self.info:
            tag = intent['Intent'].lower().replace(" ", "_")
            pattern = intent['Text']
            response = intent['Want To']
            self.addInfo(tag, pattern, response)
        
        for intent in self.info:
            tag = intent['Intent'].lower().replace(" ", "_")
            pattern = intent['Text']
            response = intent['Want To']
            self.addInfo(tag, pattern, response)
        
        for res in self.result:
            for field in res:
                # remove duplicates
                if field == "patterns":
                    auxArray = self.removeDuplicates(res[field])
                    res[field] = auxArray
                elif field == "responses":
                    auxArray = self.removeDuplicates(res[field])
                    res[field] = auxArray

        jsonString = json.dumps(list(self.result))
        jsonFile = open("dataset_covid.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()




data_file = open('corona.json').read() 
info = json.loads(data_file)
result = {
            "intents": [
                {
                    "tag": "greeting",
                    "patterns": ["Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day"],
                    "responses": ["Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"],
                    "context": [""]
                },
                {
                    "tag": "health_authority_recommendations",
                    "patterns": [""],
                    "responses": [""],
                    "context": [""] 
                }
            ]
        }

parser = Parser(result, info)
parser.start()