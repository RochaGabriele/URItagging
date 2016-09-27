import json
import random
import codecs
import os

filename = "8data.json"
output1 = "8train_data.json"
output2 = "8test_data.json"


with open(filename, "r") as f:
    data = json.load(f)
    
random.shuffle(data)

train_data = data[:int((len(data)*0.6))]
test_data = data[int((len(data)*(1 - 0.4))):]
   
with codecs.open(output1, "w", encoding="utf-8") as fp:
    json.dump(train_data, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
    
with codecs.open(output2, "w", encoding="utf-8") as fp:
    json.dump(test_data, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
