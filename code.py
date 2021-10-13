# fetching the json as a file object
# hence, json.load() will be used
# Used when dealing with large JSON files.
import json
 
# Opening JSON file
with open('input.json',"r") as input_file:
    # returns json object as a python dictionary
    data = json.load(input_file)


for result in data['results']:
    key_list = ['test_number','status','scored']
    # print(result['test_number'])
    for key in key_list:
        print(key,result[key])
        # print(key,value)
input_file.close()