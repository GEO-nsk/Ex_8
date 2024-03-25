import json

json_string = input()
doc = json.loads(json_string)

print(sorted(doc, key=lambda x: x[1], reverse=True))
