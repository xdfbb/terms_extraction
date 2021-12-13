import json
import os.path

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


f = open(base_path + "/output/structuredData.json", encoding='gbk')
json_str = data = f.read()
json_str = json_str.encode('utf-8').decode('unicode_escape')
print(json_str)