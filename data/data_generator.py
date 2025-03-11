import os 
import pandas as pd
import random
from datetime import datetime, timedelta

num_nodes = 100
num_edges = 1000
nodes = [f"NODE {i}" for i in range(num_nodes)]
start_time = datetime(2024, 3, 10, 0, 0)
time_interval_minutes = 5

data = {
    "source": [],
    "destination": [], 
    "timestamp": []
}

for _ in range(num_edges):
    source = random.choice(nodes)
    destination = random.choice([node for node in nodes if node != source])
    timestamp = start_time + timedelta(minutes=random.randint(0, num_edges) * time_interval_minutes)

    data["source"].append(source)
    data["destination"].append(destination)
    data["timestamp"].append(timestamp.strftime("%Y-%m-%d %H:%M:%S"))

df = pd.DataFrame(data)
csv_path = "../temporal_graph/data/edges.csv"
df.to_csv(csv_path, index=False)

print(df.head())