import pandas as pd
df = pd.read_json('data/example.json')

for equation in df['equation']:
    completeEquation=str(equation["x"])+ equation["operator"] + str(equation["y"])
    print(completeEquation, "=", eval(completeEquation))
