# working with json as a python string
# hence, json.loads() will be used
# Used when dealing with small json stings
import json

x = '{"name": "Bob", "languages": "English"}'

data = json.loads(x)

print(type(data))
for key,value in data.items():
    print(key,value)