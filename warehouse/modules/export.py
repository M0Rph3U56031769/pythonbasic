import json

import pandas as pd


with open(file="data.json", mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)

print(f"{'Key': <8} {'Label':<15} {'Number':<10}")
for k, v in data.get("database").items():
    label, num = v
    print("{:<8} {:<15} {:<10}".format(k, label, num))


df = pd.read_json(r'data.json')
df.to_csv(r'data.csv', index=None, header=False)
df.to_excel("d:/data.xlsx", index=None, header=False)
print(df)
